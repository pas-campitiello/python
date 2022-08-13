import wget
import re
from bs4 import BeautifulSoup

########## Get all the HTML from a text file and parse it with BeautifulSoup
with open('html.txt', 'r') as file:
    data = file.read().rstrip()

soup = BeautifulSoup(data, 'html.parser')

########## Extract all and only the MP3 URLs
i=1
urls = []
f = open("logFilesDownloaded.txt", "w")

for link in soup.find_all('div'):
   
    possibleGoodUrl = str(link.get('jsdata'))
    
    if possibleGoodUrl != "None":
        #print("possibleGoodURL = " + possibleGoodUrl)

        afterHTTPS = re.split('(https)', possibleGoodUrl)
        
        if len(afterHTTPS)==3:
            afterMP3 = re.split('(mp3)', afterHTTPS[2])
            
            if len(afterMP3)==3:
                finalURL = "https" + afterMP3[0] + afterMP3[1]

                ########## Download URLs one by one
                print("--- " + str(i) + " --- Downloading: " + finalURL)
                response = wget.download(finalURL, str(i)+".mp3")
                f.write(finalURL)
                f.write('\n')
                i=i+1
                print('\n')

f.close()
