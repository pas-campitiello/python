# You want to extract from a text in input all the URLs pointing to file based on an extension.
# For example, you have the HTML of a page and you want to extract all the PDF files referenced in that page
# which in the background have a URL to a .PDF.
# Just change the extension of the type of file you want to download --> extensionToDownload.

import re
import wget
from urllib.error import HTTPError

def Find(string):  
    # findall() has been used 
    # with valid conditions for urls in string
    #regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    
    regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    urls = re.findall(regex,string)      
    #return [x[0] for x in urls]
    return urls
      
########## Get the text to parse
with open('html.txt', 'r') as file:
    inputText = file.read().rstrip()

########## Get and clean all URLs
extensionToDownload = ".mp3"
cleanURLs = []
rawURLs = Find(inputText)
print("Found " + str(len(rawURLs)) + " URLs")

for rawURL in rawURLs:
    if extensionToDownload in rawURL:
        cleanURL = rawURL.split(extensionToDownload,1)[0] + extensionToDownload
        cleanURLs.append(cleanURL)
        #print(cleanURL)

print("of which " + str(len(cleanURLs)) + " URLs containing " + extensionToDownload)

########## Remove possible duplicates
cleanURLsUnique = set(cleanURLs)
print("of which " + str(len(cleanURLsUnique)) + " unique URLs, after removing duplicates.")
 
########## Download all URLs one by one
i=1
for URLtoDownload in cleanURLsUnique:
    try:
    	print("\n\n--- " + str(i) + " --- Downloading: " + URLtoDownload)
    	response = wget.download(URLtoDownload)    
    except HTTPError as err:
    	print("\n\nHTTPError: {0}".format(err))
    i+=1

print("\n\n")




