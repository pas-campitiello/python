#! /usr/bin/python3

#with open('Problem11-numbers.txt') as f:
#    w, h = [int(x) for x in next(f).split()] # read first line
#    array = []
#    for line in f: 
#        print(line);

numberList = []
f = open('Problem11-numbers.txt')
for line in f:
    numberList.append(int(line))

print("Number list:")
print(numberList)
print("Number list sum:" + str(sum(numberList)))

