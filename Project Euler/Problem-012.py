#! /usr/bin/python3
import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)

def triangularNumberOf(n):
    res = 0
    for i in range(1, n+1):
        res = res + i
    return res

for i in range(0,50000):
    triangularNum = triangularNumberOf(i)
    divisors = list(divisorGenerator(triangularNum))
    print(str(i) + ") " + str(triangularNum) + " -> " + str(len(divisors)))
    if len(divisors) > 500:
        break
