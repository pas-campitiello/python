# See: https://stackoverflow.com/questions/33427504/how-can-i-scrape-the-first-link-of-a-google-search-with-beautiful-soup?rq=1

import requests, urllib.parse, sys
from bs4 import BeautifulSoup

#research_later = "Zygmunt Bauman"
research_later = sys.argv[1]
google_search = "https://www.google.com.au/search?q=" + urllib.parse.quote_plus(research_later)

read_data = requests.get(google_search)

soup = BeautifulSoup(read_data.text, "html.parser")

print("This URL: " + google_search + " produced:\n")
#print(soup)

# all the results are in the tags <cite>
print("First 10 results:")
i=1
for cite in soup.find_all('cite'):
    print(str(i).rjust(2) + " - " + cite.text)
    i+=1

# first result in the first tag <cite>
print("\nFirst result: " + soup.find('cite').text)

