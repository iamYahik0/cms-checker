from multiprocessing.dummy import Pool
import requests, re, concurrent.futures, sys, os

r = '\x1b[31m'
g = '\x1b[32m'

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if not os.path.isdir('results'):
    print("Bitch Folder Not Exists")
    os.mkdir('results/')

lala = sys.argv[1]

def logo():
    x = '''CMS Checker | Developer @Sh0ya1337 | V1.0'''
    print("\x1b[1;31m"+x+"\x1b[0m \n")

def DetectCMS(site):
    ## List Of Page
    Robots0 = '{}robots.txt'.format(site)
    Joomla1 = '{}administrator/index.php'.format(site)
    Joomla2 = '{}plugins/system/debug/debug.xml'.format(site)
    Joomla3 = '{}administrator/language/en-GB/install.xml'.format(site)
    Opcart1 = '{}admin/index.php'.format(site)
    Opcart2 = '{}admin/view/javascript/common.js'.format(site)
    Bitrix1 = '{}bitrix/admin/'.format(site)

    ## List Of Requests
    CheckRaw0 = requests.get(site, headers=UA, timeout=20).text.lower()
    CheckRob0 = requests.get(Robots0, headers=UA, timeout=20).text.lower()
    CheckJom1 = requests.get(Joomla1, headers=UA, timeout=20).text.lower()
    CheckJom2 = requests.get(Joomla2, headers=UA, timeout=20).text.lower()
    CheckJom3 = requests.get(Joomla3, headers=UA, timeout=20).text.lower()
    CheckOpc1 = requests.get(Opcart1, headers=UA, timeout=20).text.lower()
    CheckOpc2 = requests.get(Opcart2, headers=UA, timeout=20).text.lower()
    CheckBit1 = requests.get(Bitrix1, headers=UA, timeout=20).text.lower()

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
    except:
        print(r+" Invalid >> "+site)

def AdvCheck(domain):
        for path in ['/','/blog/','/forum/','/test/']:
            try:
                ne_w='http://'+domain+path
                snew=requests.get(ne_w, headers=UA, timeout=20).status_code
                if snew==200:
                    DetectCMS(ne_w)
                else:
                    print(r+" !!!200 >> "+ne_w)
            except:
                print(r+" Invalid >> "+domain)
                break
if __name__ == '__main__':
    logo()
    try:
        Target = "list/"+lala
        TEXTList = open(Target, 'r').read().splitlines()
        try:
            with concurrent.futures.ThreadPoolExecutor(250) as executor:
                executor.map(AdvCheck, TEXTList)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
