# Importing Modules

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import os
import pdfkit

# Getting All site Information

http = urllib3.PoolManager()
url = "https://www.javatpoint.com"
r = http.request('GET', url)
soup = BeautifulSoup(r.data, 'html.parser')
allContent = soup.findAll('fieldset', attrs={'class': 'gra1'})

# Manipulating Site Information 

fieldNames = []
topics = []
for field in allContent:
    headline = field.find('h2').text
    fieldNames.append(headline)
    contentNames = field.findAll('p')
    contentLinks = field.findAll('a')
    fields = []
    for i in range(len(contentNames)):
        if(contentLinks[i]['href'][0:4]!='http'):
            contentLinks[i]['href'] = 'http://www.javatpoint.com/' + contentLinks[i]['href']
        fields.append((contentNames[i].text, contentLinks[i]['href']))
    topics.append(fields)
    
# Define User Choice
    
def getIndex(fieldNames):
    try:
        ind = int(input('Select one index: '))
        if(ind>0 and ind<=len(fieldNames)):
            return ind
        else:
            print('Please be a human!')
            return getIndex(fieldNames)
    except:
        print('Please Select a number')
        return getIndex(fieldNames)
    
# All Topics

for i in range(len(fieldNames)):
    print('{0}. {1}'.format(i+1, fieldNames[i]))
    for x in topics[i]:
        print('\t{0}'.format(x[0]))
        
    
# Get User choice

ind1 = getIndex(fieldNames)
for i in range(len(topics[ind1-1])):
    print('{0}. {1}'.format(i+1, topics[ind1-1][i][0]))
ind2 = getIndex(topics[ind1-1])

topicNameDecided = topics[ind1-1][ind2-1][0]
topicLinkDecided = topics[ind1-1][ind2-1][1]
print(topics[ind1-1][ind2-1][0], topics[ind1-1][ind2-1][1])

# Getting Modules

http = urllib3.PoolManager()
url = topicLinkDecided
r = http.request('GET', url)
soup = BeautifulSoup(r.data, 'html.parser')

# Creating Modules

moduleTags = soup.findAll('h2', attrs={'class': 'spanh2'})
modules = []
for module in moduleTags:
    modules.append(module.text)

for module in modules:
    if not os.path.exists(module):
        os.makedirs(module)
        
# Creating HTML files from each modules

reqNo=0
contentTable = soup.findAll('div', attrs={'class': 'leftmenu'}) # Index

for i in range(len(contentTable)):
    links = []
    for x in contentTable[i]:
        a = str(x)
        y = "href="
        i1 = a.find(y)
        if(i1==-1): # No Links
            continue
        i1+=6 # Skip <"a href=">
        i2 = a.find('\"', i1)  # Find Ending quote
        links.append(a[i1:i2]) # a[i1:i2] is the final href
    print(links)
    for link in links:
        reqNo+=1
        print("Request Number:" + str(reqNo))
        url = "http://www.javatpoint.com/" + link
        r = http.request('GET', url)
        soup = BeautifulSoup(r.data, 'html.parser')
        [s.extract() for s in soup('script')]  # Remove Scripts
        [s.extract() for s in soup('ins')]     # Remove Ads
        [s.extract() for s in soup('iframe')]  # Remove Ads2
        mainContent = soup.find('div', attrs={'id': 'city'})

        # For Images
        images = mainContent.findAll('img')
        for x in range(len(images)):
            imageSrc = images[x]['src']
            imageSrc = str(imageSrc)
            if(imageSrc.find('static.javatpoint.com')==-1):
                images[x]['src'] = 'http://javatpoint.com' + images[x]['src']

        for x in range(len(images)):
            mainContent.findAll('img')[x]['src']=images[x]['src']
            
        # For CodeBlock
        codes = mainContent.findAll('textarea', attrs= {'name': 'code'})
        for c in range(len(codes)):
            newTag = soup.new_tag('p')
            newTag.append(str(codes[c].get_text()))
            mainContent.find('textarea').replaceWith(newTag)

        # Final HTML
        mainContent = str(mainContent).replace("\n"," ")
        header = "<html> <head> <meta charset='UTF-8'> <link rel=\"stylesheet\" type=\"text/css\" href=\"./../javatpoint.css\"> </head>  <body>"
        footer = "</body></html>"
        mainContent = header + mainContent + footer
        try:
            f = open("./" + modules[i] + "/" + link + ".html", "w")
            for ch in mainContent:
                try:
                    f.write(ch)
                except:
                    f.write(" ")
            f.close()
        except:
            print("Can't Create " + str(link) + ".html")
            
# Sorting HTML according to creation time

def sorted_dir(folder):
    def getctime(name):
        path = os.path.join(folder, name)
        return os.path.getctime(path)
    return sorted(os.listdir(folder), key=getctime)

# For Windows only
# path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
# config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)


# Converting each module to PDF

for x in range(len(modules)):
    myList = sorted_dir(modules[x])
    for i in range(len(myList)):
        myList[i]=modules[x] + "/" + myList[i]
    pdfkit.from_file(myList, modules[x] + '.pdf')