print("\n----- modify the content of an existing file -----\n")

f = open("contentfile.txt", "r")
contents = f.readlines()
f.close()

print(contents)
contents.insert(2, "New line in the middle of the content file\n")

f = open("contentfile.txt", "w")
contents = "".join(contents)
f.write(contents)
f.close()

print()
f = open('contentfile.txt')
for line in f:
    print(line, end='')


with open('contentfile.txt', 'a') as f3:
    f3.write("New line appended at the end of the content file.\n")
    
with open('contentfile.txt') as f3:
    read_data = f3.read()
    print ("File content again:")
    print(read_data)

print("\n----- create a new file -----\n")

f = open("contentfile2.txt", "w")
contents = f.write("Content in the new file\n")
f.close()

with open('contentfile.txt') as f3:
    read_data = f3.read()
    print ("File content:")
    print(read_data)
