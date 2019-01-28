import urllib.request
import httplib2
import bs4 as bs
from bs4 import SoupStrainer

url = 'https://www.example.org'

extensionToParse = '.mp3'
path='/home/myfolder/'

http = httplib2.Http()
status, response = http.request(url)

for link in bs.BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):
    if ((link.has_attr('href')) and (extensionToParse in link['href'])):
        url = link['href']
        filename = url[url.rfind("/")+1:]
        print('URL: ' + url)
        print('Downloading: ' + filename)
        urllib.request.urlretrieve(link['href'], path+filename)
        print('---')

