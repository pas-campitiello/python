import sys
import pandas as pd
from bs4 import BeautifulSoup

def printTableContent(table_to_print):
    row_marker = 0
    for row in table_to_print.find_all('tr'):

        sys.stdout.write(str(row_marker) + " - ")   # sys.stdout.write to avoid new line after the write

        column_marker = 0
        columns = row.find_all('td')
        if (not columns):
            columns = row.find_all('th')

        for column in columns:
            sys.stdout.write(str(column_marker) + "[" + column.get_text() + "]" + "  \t")
            column_marker += 1
     
        row_marker+=1   
        print()
    
def writeTableToFile(table_to_write, filename, separator):
    with open(filename, "w") as f:
        for row in table_to_write.find_all('tr'):
            columns = row.find_all('td')
            if (not columns):
                columns = row.find_all('th')
            for column in columns:
                f.write(column.get_text() + separator)
            f.write("\n")

with open("table-input2.htm", "r") as f:
    read_data = f.read()
    print("File content:")
    print(read_data)

soup = BeautifulSoup(read_data, 'lxml') # Parse the HTML as a string
table1 = soup.find_all('table')[0]      # Grab the first table
table2 = soup.find_all('table')[1]      # Grab the second table

print("This is the first table: \n" + str(table1))
print()
print("This is the second table: \n" + str(table2))
print()

print("Content first table:")
printTableContent(table1)
print()
print("Content second table:")
printTableContent(table2)

print()
print("Writing first table to file table1ToFile.csv, values comma separated")
writeTableToFile(table1,"table1ToFile.csv",",")
print("Writing first table to file table2ToFile.csv, values tab separated")
writeTableToFile(table2,"table2ToFile.csv","\t")

