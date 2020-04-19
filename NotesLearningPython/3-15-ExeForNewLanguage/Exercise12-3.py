import collections

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

def listWordsInFile(filename):
    fileToRead = open(filename)
    words = fileToRead.read().split()
    fileToRead.close()
    return words

def countWordInList(listOfWords, wordToSearch):
    c = collections.Counter(listOfWords)
    print("The word '", wordToSearch, "' has been found ", c[wordToSearch], " times.")

openAndPrintFile("fileToAnalyze.txt")
words = listWordsInFile("fileToAnalyze.txt")

print(words)
print("-------------------------------------")
countWordInList(words,"and")
countWordInList(words,"Terre")
countWordInList(words,"PUTIN")
