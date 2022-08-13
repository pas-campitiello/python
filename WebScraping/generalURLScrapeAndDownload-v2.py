# Python code to find the URL from an input string
# Using the regular expression
# source: https://www.geeksforgeeks.org/python-check-url-string/#:~:text=To%20find%20the%20URLs%20in,returned%20in%20the%20order%20found.
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
      
########## Get all the HTML from a text file
extensionToDownload = ".mp3"
cleanURLs = []

with open('html.txt', 'r') as file:
    inputText = file.read().rstrip()

########## Get and clean all URLs
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






