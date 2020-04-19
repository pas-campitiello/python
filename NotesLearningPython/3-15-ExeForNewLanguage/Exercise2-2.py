init = 0
prec = 0    
next = 1

while next < 1000:
    prec = next     
    next = next + init
    init = prec
    print(next)

