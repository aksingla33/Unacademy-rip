# coding: utf-8
 
 
import requests
import os
import urllib
import img2pdf
from lxml import html
from zipfile import ZipFile 
from bs4 import BeautifulSoup, SoupStrainer
import urllib2


urla = urllib2.urlopen("https://unacademy.com/lesson/1st-june-2017-daily-mcqs-on-current-affairs-for-government-exams-upsc-cseias-exam/PKSYUA6X").read()


soup = BeautifulSoup(urla)
a =[]
for line in soup.find_all('a'):
    links = line.get('href')
    links = str(links)
    if "lesson" in links:
        if "/comment/" not in links:
            #if links.startswith('/lesson/'):
            if links not in a:
                a.append(links)
#print(links)
#print(a)
num = 0
for item in a:
    url  = "https://unacademy.com" + item
    num = num + 1
     
    url_data = requests.get(url)
    
     
     
    tree = html.fromstring(url_data.content)
    
     
     
    test_data = tree.xpath("//meta[@itemprop='image']//@content")
    
    
     
    lession_id = test_data[0].split("/")[3]
    
     
     
    img_url = []
    
    i = 0
    while 1:
        url = "http://player-images.unacademy.link/%s/images/%s.jpeg"% (lession_id, i)
        if requests.head(url).status_code == 404:
            break
        img_url.append(url)
        i = i + 1
        print url
    
     
    for i, j in enumerate(img_url):
        print "downloading", j
        urllib.urlretrieve (j, "%s.jpeg"%i)
    with open("output_%s.pdf"%num, "wb") as f:
        f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpeg")]))
    filelist = [ f for f in os.listdir(".") if f.endswith(".jpeg") ]
    for f in filelist:
        os.remove(os.path.join(".", f))
