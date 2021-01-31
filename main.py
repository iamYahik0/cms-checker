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
    ## List Of Page
    RawSite = site
    Robots0 = site+"robots.txt"
    Joomla1 = '{}administrator/index.php'.format(site)
    Joomla2 = '{}plugins/system/debug/debug.xml'.format(site)
    Joomla3 = '{}administrator/language/en-GB/install.xml'.format(site)
    Opcart1 = '{}admin/index.php'.format(site)
    Opcart2 = '{}admin/view/javascript/common.js'.format(site)
    Bitrix1 = '{}bitrix/admin/'.format(site)

    ## List Of Requests
    CheckHead = requests.get(RawSite, headers=UA, timeout=15)
    CheckRaw0 = CheckHead.text.lower()
    CheckRob0 = requests.get(Robots0, headers=UA, timeout=15).text.lower()
    CheckJom1 = requests.get(Joomla1, headers=UA, timeout=15).text.lower()
    CheckJom2 = requests.get(Joomla2, headers=UA, timeout=15).text.lower()
    CheckJom3 = requests.get(Joomla3, headers=UA, timeout=15).text.lower()
    CheckOpc1 = requests.get(Joomla3, headers=UA, timeout=15).text.lower()
    CheckOpc2 = requests.get(Joomla3, headers=UA, timeout=15).text.lower()
    CheckBit1 = requests.get(Joomla3, headers=UA, timeout=15).text.lower()

    ## List Of Checks
    ResJoomlaRobots1 = 'if the joomla site is installed' #CheckRob0
    ResJoomlaSource1 = 'content="joomla!' #CheckJom1
    ResJoomlaSource2 = 'css/joomla.css' #CheckRaw0
    ResJoomlaSource3 = '<author>joomla!' #CheckJom2||CheckJom3
    ResOpcartSource1 = 'powered by <a href="http://www.opencart.com">opencart' #CheckRaw0
    ResOpcartSource2 = 'catalog/view/javascript/jquery/swiper/css/opencart.css' #CheckRaw0
    ResOpcartSource3 = 'index.php?route=' #CheckRaw0
    ResOpcartSource4 = 'common/login' #CheckOp1
    ResOpcartSource5 = 'geturlvar(key)' #CheckOpc2
    ResDrupalRobots1 = 'allow: /core/*.css$' #CheckRob0
    ResDrupalRobots2 = 'disallow: /index.php/user/login/' #CheckRob0
    ResDrupalRobots3 = 'disallow: /web.config' #CheckRob0
    ResDrupalSource1 = '/misc/drupal.js' #CheckRaw0
    ResMagentSource1 = 'x-magento-init' #CheckRaw0
    ResMagentSource2 = '/skin/frontend/' #CheckRaw0
    ResMagentSource3 = '/mage/cookies.js' #CheckRaw0
    ResBitrixSource1 = '/bitrix/js/main/' #CheckBit1
    ResMODXSource1 = 'powered by modx' #CheckRaw0
    try:
        if ResJoomlaRobots1 in CheckRob0 or ResJoomlaSource1 in CheckJom1 or ResJoomlaSource2 in CheckRaw0 or ResJoomlaSource3 in CheckJom2 or ResJoomlaSource3 in CheckJom3:
            print(g+" Joomla >> "+site)
            open('results/joomla-'+lala+'.txt','a').write(site+'\n')
        elif ResOpcartSource1 in CheckRaw0 or ResOpcartSource2 in CheckRaw0 or ResOpcartSource3 in CheckRaw0 or ResOpcartSource4 in CheckOpc1 or ResOpcartSource5 in CheckOpc2:
            print(g+" Opencart >> "+site)
            open('results/opencart-'+lala+'.txt','a').write(site+'\n')
        elif ResDrupalRobots1 in CheckRob0 or ResDrupalRobots2 in CheckRob0 or ResDrupalRobots3 in CheckRob0 or ResDrupalSource1 in CheckRaw0:
            print(g+" Drupal >> "+site)
            open('results/drupal-'+lala+'.txt','a').write(site+'\n')
        elif ResMODXSource1 in CheckRaw0:
            print(g+" MODX >> "+site)
            open('results/modx-'+lala+'.txt','a').write(site+'\n')
        elif ResBitrixSource1 in CheckBit1:
            print(g+" Bitrix >> "+site)
            open('results/bitrix-'+lala+'.txt','a').write(site+'\n')
        elif ResMagentSource1 in CheckRaw0 or ResMagentSource2 in CheckRaw0 or ResMagentSource3 in CheckRaw0 :
            print(g+" Magento >> "+site)
            open('results/magento-'+lala+'.txt','a').write(site+'\n')
        else:
            print(g+" Unknown >> "+site)
            open('results/unknown-'+lala+'.txt','a').write(site+'\n')
    except Exception as e:
        #print(e)
        print(r+" Invalid >> "+site)

def AdvCheck(domain):
        for path in ['/','/blog/','/forum/','/forums/', '/shop/']:
            try:
                ne_w='http://'+domain+path
                checkres = requests.get(RawSite, headers=UA, timeout=20).status_code
                if checkres == "200":
                    DetectCMS(ne_w)
            except Exception as e:
                #print(e)
                print(r+" Invalid >> "+ne_w)
if __name__ == '__main__':
    logo()
    try:
        Target = "list/"+lala
        TEXTList = open(Target, 'r').read().splitlines()
        try:
            with concurrent.futures.ThreadPoolExecutor(350) as executor:
                executor.map(AdvCheck, TEXTList)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
