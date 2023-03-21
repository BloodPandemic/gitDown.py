from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, os, platform

def searchQuery(query: str):
    query = Query(query)
    html = urlopen('https://github.com/search?q={}'.format(query))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.findAll('a', {'class':'v-align-middle'})
    return links

def detect_linux_distribution():
    #Detect the Linux distribution on which the Python script is running.
    dist = platform.linux_distribution(full_distribution_name=False)
    if dist[0].lower() == 'ubuntu':
        return 'Ubuntu'
    elif dist[0].lower() == 'debian':
        return 'Debian'
    elif dist[0].lower() == 'centos':
        return 'CentOS'
    elif dist[0].lower() == 'fedora':
        return 'Fedora'
    else:
        return None
    
def Query(query):
    space = ' '
    if space in query:
        query = query.replace(space, '%20')
    return query

def downloadProj(num: int, query: str):
    links = searchQuery(query)
    try:
        os.system('git clone https://github.com/{}.git'.format(links[num]['href']))
    except Exception as e:
        print("[!] git is not install ")
        try:
            print("[?] Checking if you are sudo ....")
            if os.getuid() == 0:
                pass
            else: print("[-] Closing... Run as sudo");exit(1)
            print("[+] installing Git....")
            if detect_linux_distribution() == 'ubuntu' or detect_linux_distribution() == 'debian':
                os.system('sudo apt-get install git')
            elif detect_linux_distribution() == 'centos' or detect_linux_distribution() == 'fedora':
                os.system('sudo yum install git')
            print("Done installing git ... Proceeding to install the repository...")
            os.system('git clone https://github.com/{}.git'.format(links[num]['href']))
        except:
            print("some error occured!")

query = str(input("enter Query --> "))
links = searchQuery(query)
for i in range(0, len(links)):   
    print(links[i]['href'])
    print(i)
        #print(list(i for i in range(0, len(links))))
    print("<========================================================>\n")
while True:
    try:
        option = int(input("Enter which repo u want to get: "))
        downloadProj(option, query)
    except KeyboardInterrupt as e:
        exit(1)
    except TypeError as k:
        print("Enter a number")