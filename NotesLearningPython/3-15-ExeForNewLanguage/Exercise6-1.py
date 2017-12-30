import operator, math

print("---- addition, subtraction, multiplication, division ----\n")

print("2+3                      =", 2+3)
print("operator.add(2,3)        =", operator.add(2,3) )
print("8-1                      =", 8-1)
print("operator.sub(8,1)        =", operator.sub(8,1) )
print("9*7                      =", 9*7)
print("operator.mul(9,7)        =", operator.mul(9,7) )
print("15/4                     =", 15/4)
print("operator.truediv(15,4)   =", operator.truediv(15,4))
print("15//4                    =", 15//4)
print("operator.floordiv(15,4)  =", operator.floordiv(15,4))

print("\n---- square-root, square, cube ----\n")
print("12**0.5              =", 12**0.5)
print("math.sqrt(12)        =", math.sqrt(12))
print("math.pow(81,1/4)     =", math.pow(81,1/4))
print("math.pow(2,3)        =", math.pow(2,3))
print("3**3                 =", 3**3)
print("operator.pow(3,2)    =", operator.pow(3,2))

print("\n---- sin, cos, tan ----\n")
print("math.sin(90) =", math.sin(90))
print("math.cos(90) =", math.cos(90))
print("math.tan(90) =", math.tan(90))

print("\n---- factorial, inverse, modulus ----\n")
print("math.factorial(5)    =", math.factorial(5))
print("abs(-34)             =", abs(-34))
print("operator.abs(-66)    =", operator.abs(-66))
print("10 % 3               =", 10 % 3)
print("divmod(10,3)         =", divmod(10,3))
print("divmod(10,3)[0]      =", divmod(10,3)[0])
print("divmod(10,3)[1]      =", divmod(10,3)[1])
print("fmod(10,3)           =", math.fmod(10,3))

