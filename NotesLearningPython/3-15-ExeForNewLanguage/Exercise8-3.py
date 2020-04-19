import os

print("\n----- rename a file -----\n")

os.rename("contentfile2.txt", "new_name_contentfile2.htm")

with open('new_name_contentfile2.htm') as f3:
    read_data = f3.read()
    print ("File content again:")
    print(read_data)

try:
    with open('contentfile2.txt') as f3:
        read_data = f3.read()
        print ("File content:")
        print(read_data)
except FileNotFoundError:
    print("File named contentfile2.txt not found!")

print("\n----- delete a file in a folder -----\n")

os.remove("new_name_contentfile2.htm")

try:
    with open('new_name_contentfile2.htm') as f3:
        read_data = f3.read()
        print ("File content:")
        print(read_data)
except FileNotFoundError:
    print("File named new_name_contentfile2.htm not found!")

