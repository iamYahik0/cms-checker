import requests
import concurrent.futures
import threading
import sys
import os

opl = sys.argv[1]

if not os.path.isdir('results'):
    print("Bitch Folder Not Exists")
    os.mkdir('./results/')
else:
    print("Bitch Folder Exists")

r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

def DetectCMS(site):
    Joomla = 'http://{}/administrator/help/en-GB/toc.json'.format(site)
    Joomla2 = 'http://{}/administrator/language/en-GB/install.xml'.format(site)
    Joomla3 = 'http://{}/plugins/system/debug/debug.xml'.format(site)
    Joomla4 = 'http://{}/administrator/'.format(site)
    Opencart2 = 'http://{}/admin/index.php'.format(site)
    Opencart = 'http://{}/admin/view/javascript/common.js'.format(site)
    try:
        CheckJom = requests.get(Joomla, timeout=20, headers=Headers).content
        CheckJom2 = requests.get(Joomla2, timeout=20, headers=Headers).content
        CheckJom3 = requests.get(Joomla3, timeout=20, headers=Headers).content
        CheckJom4 = requests.get(Joomla4, timeout=20, headers=Headers).content
        CheckOpencart = requests.get(Opencart, timeout=20, headers=Headers).content
        CheckOpencart2 = requests.get(Opencart2, timeout=20, headers=Headers).content
        if '"COMPONENTS_BANNERS_BANNERS"' in str(CheckJom):
            with open('./results/joomla-'+opl+'.txt', 'a') as XW:
                XW.write('http://'+site+'/administrator/index.php \n')
            print(g+" + "+site+" --> Joomla")
        elif '<author>Joomla!' in str(CheckJom2):
            with open('./results/joomla-'+opl+'.txt', 'a') as XW:
                XW.write('http://'+site+'/administrator/index.php \n')
            print(g+" + "+site+" --> Joomla")
        elif '<author>Joomla!' in str(CheckJom3):
            with open('./results/joomla-'+opl+'.txt', 'a') as XW:
                XW.write('http://'+site+'/administrator/index.php \n')
            print(g+" + "+site+" --> Joomla")
        elif 'content="Joomla!' in str(CheckJom4):
            with open('./results/joomla-'+opl+'.txt', 'a') as XW:
                XW.write('http://'+site+'/administrator/index.php \n')
            print(g+" + "+site+" --> Joomla")
        elif 'common/login' in str(CheckOpencart2):
            with open('./results/opencart-'+opl+'.txt', 'a') as XW:
                XW.write('http://'+site+'/admin/index.php \n')
            print(g+" + "+site+" --> Opencart")
        elif 'getURLVar(key)' in str(CheckOpencart):
            with open('./results/opencart-'+opl+'.txt', 'a') as XW:
                XW.write('http://'+site+'/admin/index.php \n')
            print(g+" + "+site+" --> Opencart")
        else:
            print(r+" + "+site+" --> Unknowm")
            with open('./results/unknown-'+opl+'.txt', 'a') as XW:
                XW.write(site + '\n')
    except:
        print(r+" - "+site+" --> Invalid")


if __name__ == '__main__':
    try:
        Target = "list/"+opl
        TEXTList = open(Target, 'r').read().splitlines()
        try:
            with concurrent.futures.ThreadPoolExecutor(200) as executor:
                executor.map(DetectCMS, TEXTList)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
