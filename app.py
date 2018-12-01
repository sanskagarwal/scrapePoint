# Importing Modules

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import os


# Creating Modules
modules = ["java-tutorial","java-string","exception-handling-in-java","multithreading-in-java","java-io","java-awt"]
for module in modules:
    if not os.path.exists(module):
        os.makedirs(module)

# Creating HTML files from each modules

http = urllib3.PoolManager()
reqNo=0
for module in modules:
    url = "http://www.javatpoint.com/" + module
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, 'html.parser')
    contentTable = soup.findAll('div', attrs={'class': 'leftmenu'})
    links = []
    for i in range(len(contentTable)):
            for x in contentTable[i]:
                a = str(x)
                y = "href="
                i1 = a.find(y)
                if(i1==-1):
                    continue
                i1+=6
                i2 = a.find('\"', i1)
                links.append(a[i1:i2])
    for link in links:
        reqNo+=1
        print("Request Number:" + str(reqNo))
        url = "http://www.javatpoint.com/" + link
        r = http.request('GET', url)
        soup = BeautifulSoup(r.data, 'html.parser')
        [s.extract() for s in soup('script')]
        [s.extract() for s in soup('ins')]
        mainContent = soup.find('div', attrs={'id': 'city'})
        mainContent = str(mainContent).replace("\n"," ")
        pageLen = len(mainContent)
        for i in range(pageLen-2):
            if(mainContent[i]=='s' and mainContent[i+1]=='r' and mainContent[i+2]=='c' and mainContent[i+3]=='='):
                mainContent = mainContent[:i+5] + "http://www.javatpoint.com/" + mainContent[i+5:]
                i+=31
        header = "<html> <head> <link rel=\"stylesheet\" type=\"text/css\" href=\"./../javatpoint.css\"> </head>  <body>"
        footer = "</body></html>"
        mainContent = header + mainContent + footer
        try:
            f = open("./" + module + "/" + link + ".html", "w")
            for ch in mainContent:
                try:
                    f.write(ch)
                except:
                    f.write(" ")
            f.close()
        except:
            print("Can't Create " + str(link) + ".html")