import operator, math, decimal

def truncateDecimals1(strNum, x):
    posDot = strNum.index(".")
    print(" dot position =", posDot)
    print(" int part .   =", strNum[:posDot+1]) 
    print(" decimal part =", strNum[posDot+1:posDot+x+1])
    return strNum[:posDot+1] + strNum[posDot+1:posDot+x+1]

def truncateDecimals2(strNum, x):
    before_dec, after_dec = str(strNum).split('.')
    return float('.'.join((before_dec, after_dec[0:x])))    

def truncateDecimals3(num):
    return decimal.Decimal(num).quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_DOWN)

def truncateDecimals4(num, x):
    return math.floor(num * 10**x) / 10**x

print("---- rounding up to 5 decimal places ----\n")

num = float(input("Insert a float number: "))

print("math.ceil(num) =", math.ceil(num))
print("round(num)     =", round(num))
print("round(num,4))  =", round(num,4) )
print("round(num,5))  =", round(num,5) )
print("'%.5f' % num   =", "%.5f" % num )
print("math.pi        =", math.pi )
print("'%5.3f' % num  =", "%5.3f" % math.pi )

print("\n---- truncating after 4 decimal places ----\n")
print("math.trunc(num)                  =", math.trunc(num))
print("str(num)[:6]                     =", str(num)[:6])
print("truncateAtDecimals1(str(num),4)) =", float(truncateDecimals1(str(num),4)))
print("truncateAtDecimals2(str(num),4)) =", truncateDecimals2(str(num),4))
print("truncateAtDecimals3(num))        =", truncateDecimals3(num))
print("truncateAtDecimals4(num,4))      =", truncateDecimals4(num,4))

print("\n---- padding zeros to the right and left ----\n")
print("str(num).zfill(5)        =", str(num).zfill(5))
print("'-42'.zfill(5)           =", "-42".zfill(5))
print("str(num).center(20,'0')  =", str(num).center(20,"0"))
print("str(num).rjust(20,'0')   =", str(num).rjust(20,"0"))
print("str(num).ljust(20,'0')   =", str(num).ljust(20,"0"))
print("'{0:03f}'.format(num)    =",'{0:03f}'.format(num))
print('%(thisword)s is this one %(number)05f with 5 padding zeros right.' % {'thisword': "Your number", "number": num})
print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})

print("\n---- right and left justification ----\n")
print("str(num).rjust(20,' ')   =", ">", str(num).rjust(20," "), "<")
print("str(num).ljust(20,' ')   =", ">", str(num).ljust(20," "), "<")

