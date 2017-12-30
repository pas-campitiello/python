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

file = open("fileToAnalyze.txt", "r", encoding="utf-8-sig")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
file.close()

uniqueWords = []
uppercaseWords = []
for k,v in wordcount.items():
    if k.isupper():
        uppercaseWords.append(k)
    if v==1: 
        print("{0:15} ==> {1}".format(k,v))
        uniqueWords.append(k)
    else:
        print("{0:20} ==> {1}".format(k,v))

print("-------------------------------------")
print("Unique words: ", uniqueWords)
print("-------------------------------------")
print("Uppercase words: ", uppercaseWords)
