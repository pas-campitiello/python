import textwrap

def openAndPrintFile(filename):
    f = open(filename)  # read mode "r" is set up by default
    print ("Name of the file: ", f.name)
    print("-------------------------------------")
    c = 0
    for line in f:
        print(str(c) + " - " + line, end='')
        c += 1
    print("-------------------------------------")
    f.close()

def readFileInAString(fileName):
    with open(fileName) as f3:
        return f3.read()

openAndPrintFile("fileToWordWrap.txt")

lineWidth = int(input("Input line width: "))

wrapped_text = textwrap.wrap(readFileInAString("fileToWordWrap.txt"), lineWidth)
print("\nText wrapped:\n")
print(wrapped_text)
print()
for line in wrapped_text:
    print(line)
