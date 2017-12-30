# See: https://www.goodreads.com/api/

import requests, urllib.parse, sys
from bs4 import BeautifulSoup

def getAuthorInfo(author_search_str, key):
    goodreads_search_author_info = "https://www.goodreads.com/api/author_url/" + urllib.parse.quote_plus(author_search_str) + "?key=" + key
    read_data = requests.get(goodreads_search_author_info)
    soup = BeautifulSoup(read_data.text, "html.parser")

    # print("This URL: " + goodreads_search_author_info + " produced:\n")
    # print(soup.prettify())
    print("\nData of the closest Goodreads author:\n")

    author_id   = soup.find('author')['id']
    author_name = soup.find('name').text
    author_link = soup.find('link').next_sibling
    print(str("ID:").ljust(8) + author_id)
    print(str("Name:").ljust(8) + author_name)
    print(str("Link:").ljust(8) + author_link)

    return [author_id, author_name, author_link]

def getAuthorBooksData(author_id, key):

    print("\nBooks by this author:\n")

    goodreads_search_books_by_author = "https://www.goodreads.com/author/list.xml?key=" + key + "&id=" + author_id
    #goodreads_search_books_by_author = "https://www.goodreads.com/author/list.xml?key=" + key + "&id=" + author_id + "&page=1&per_page=200"
    
    read_data = requests.get(goodreads_search_books_by_author)
    soup = BeautifulSoup(read_data.text, "html.parser")

    print("This URL: " + goodreads_search_books_by_author + " produced:\n")
    # print(soup.prettify())
    
    #author_id   = soup.find('author')['id']
    #author_name = soup.find('name').text
    #author_link = soup.find('link').next_sibling
    
    print("Total number of books: " + soup.find('books')['total'])
    print()
    i=1
    for book in soup.find_all('book'):
        print("\n---" + str(i) + " -------------------- \n")
        print("ID: ".ljust(15) + book.find('id').text)
        print("Title: ".ljust(15) + book.find('title').text)
        print("Num pages: ".ljust(15) + book.find('num_pages').text)
        print("Year: ".ljust(15) + book.find('publication_year').text)
        print("AVG rating: ".ljust(15) + book.find('average_rating').text)
        print("Num ratings: ".ljust(15) + book.find('ratings_count').text)
        print("Points: ".ljust(15) + str(float(book.find('average_rating').text) * float(book.find('ratings_count').text)))
        i+=1

key = "d6XqV6grF2Rz7Cs0WJesuQ"
#secret = 
#author_search_str = "Giovanni Rana"
author_search_str = sys.argv[1]

author_data = getAuthorInfo(author_search_str, key)
getAuthorBooksData(author_data[0], key)


