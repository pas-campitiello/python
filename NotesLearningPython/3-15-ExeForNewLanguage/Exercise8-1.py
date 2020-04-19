import os

print("----- list files in folder -----\n")

print("Files in the current folder:\n", os.listdir())
print("\nFiles in the root folder:\n", os.listdir('/'))

print("\n----- read and print content of a file -----\n")

f = open('contentfile.txt')
print ("Name of the file: ", f.name)
for line in f:
    print(line, end='')

with open('contentfile.txt') as f:
    read_data = f.read()
    print ("File content again:")
    print(read_data)

f2 = open('../1-VersionsAndSetup.md')
print ("Name of the file: ", f2.name)
line = f2.readlines()
print ("Read lines: %s" % (line))

f2.close()
