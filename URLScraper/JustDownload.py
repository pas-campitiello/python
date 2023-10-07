# You want to extract from a text in input all the URLs pointing to file based on an extension.
# For example, you have the HTML of a page and you want to extract all the PDF files referenced in that page
# which in the background have a URL to a .PDF.
# Just change the extension of the type of file you want to download --> extensionToDownload.

import re
import wget
from urllib.error import HTTPError

urls_array = []
with open('html.txt', 'r') as my_file:
    for line in my_file:
        urls_array.append(line)

#print(set(urls_array))

########## Download all URLs one by one
i=1
for URLtoDownload in set(urls_array):
	try:
	    print("\n\n--- " + str(i) + " --- Downloading: " + URLtoDownload)
	    response = wget.download(URLtoDownload)    
	except HTTPError as err:
	    print("\n\nHTTPError: {0}".format(err))
	i+=1

print("\n\n")
