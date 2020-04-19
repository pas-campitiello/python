def searchWordInFile(word, filename):
    print("-------------------------------------")    
    f = open(filename)
    print("Searching for the word '"+word+"'...")
    c = 0
    lineCount = 0
    lines = []
    for line in f:
        if word in line: 
            c+=1
            lines.append(lineCount)
        lineCount+=1    
    print("Word '"+word+"' found " + str(c) + " times at these lines: " + str(lines))
    print("-------------------------------------")

def openAndPrintFile(filename):
    f = open(filename)  # read mode "r" is set up by default
    print ("Name of the file: ", f.name)
    print("-------------------------------------")
    c=0
    for line in f:
        print(str(c) + " - " + line, end='')
        c+=1
    print("-------------------------------------")
    f.close()

openAndPrintFile("fileToAnalyze.txt")
searchWordInFile("and", "fileToAnalyze.txt")

