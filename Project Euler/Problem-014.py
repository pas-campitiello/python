#! /usr/bin/python3

# See example down here: https://en.wikipedia.org/wiki/Collatz_conjecture

def countSteps(num):
    steps = 0
    while (num!=1):
        if ((num%2)==0):
            num = num/2
        else:
            num = (3*num+1)
        steps = steps + 1
    return steps

maxNumberOfSteps = 0
for i in range(500000,1000000):
    countedSteps = countSteps(i)+1
    #print(str(i) + " -> " + str(countedSteps))
    if (countedSteps > maxNumberOfSteps):
        maxNumberOfSteps = countedSteps
        print(str(i) + " -> " + str(maxNumberOfSteps))

