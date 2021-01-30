from multiprocessing.dummy import Pool
import requests, re, concurrent.futures, sys, platform, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

r = '\x1b[31m'
g = '\x1b[32m'

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if not os.path.isdir('results'):
    print("Bitch Folder Not Exists")
    os.mkdir('results/')

lala = sys.argv[1]

def logo():
    x = '''
    ██╗  ██╗███████╗███╗   ██╗████████╗ █████╗ ██╗
    ██║  ██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║
    ███████║█████╗  ██╔██╗ ██║   ██║   ███████║██║
    ██╔══██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║
    ██║  ██║███████╗██║ ╚████║   ██║   ██║  ██║██║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝
      CMS Checker | Developer @Sh0ya1337 | V1.0'''
    print("\x1b[1;31m"+x+"\x1b[0m \n")


def DetectCMS(site):
    try:
        Joomla0 = requests.get(site, headers=UA, verify=False, timeout=15)
        Joomla1 = Joomla0.text
        Joomla2 = requests.get('{}/administrator/'.format(site), headers=UA, verify=False, timeout=15).text
        Joomla3 = requests.get('{}/administrator/help/en-GB/toc.json'.format(site), headers=UA, verify=False, timeout=15).text
        Opencart1 = requests.get('{}/admin/view/javascript/common.js'.format(site), headers=UA, verify=False, timeout=15).text
        Opencart2 = requests.get('{}/admin/index.php'.format(site), headers=UA, verify=False, timeout=15).text
        if 'window.Joomla' in Joomla1 or 'content="Joomla!' in Joomla2 or '<author>Joomla!' in Joomla3:
            print(g+" - "+site+" --> Joomla")
            open('results/joomla-'+lala+'.txt','a').write(site+'\n')
        elif '/sites/default/' in Joomla1:
            print(g+" - "+site+" --> Drupal")
            open('results/drupal-'+lala+'.txt','a').write(site+'\n')
        elif 'laravel_session' in Joomla0.cookies:
            print(g+" - "+site+" --> Laravel")
            open('results/laravel-'+lala+'.txt','a').write(site+'\n')
        elif 'catalog/view/' in Joomla1 or 'getURLVar(key)' in Opencart1 or 'common/login' in Opencart2:
            print(g+" - "+site+" --> Opencart")
            open('results/opencart-'+lala+'.txt','a').write(site+'\n')
        else:
            print(g+" - "+site+" --> Unknown")
            open('results/unknown-'+lala+'.txt','a').write(site+'\n')
    except:
        print(r+" - "+site+" --> Invalid")

def AdvCheck(domain):
    try:
        for X in ['/','/blog','/forum','/forums', '/shop']:
            ne_a='http://'
            ne_w=ne_a+domain+X
            ktn00 = requests.get(ne_w, headers=UA, verify=False, timeout=20).status_code
            if ktn00==200:
                DetectCMS(ne_w)
    except :
        print(r+" - "+domain+" --> Invalid")

if __name__ == '__main__':
    logo()
    try:
        Target = "list/"+lala
        TEXTList = open(Target, 'r').read().splitlines()
        try:
            with concurrent.futures.ThreadPoolExecutor(200) as executor:
                executor.map(AdvCheck, TEXTList)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
