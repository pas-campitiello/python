basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # show that duplicates have been removed

print("'orange' in basket?    -", 'orange' in basket)
print("'crabgrass' in basket? -", 'crabgrass' in basket)

print("----------------------")

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print("a = ", a)        # unique letters in a
print("b = ", b)        # unique letters in b

print("a - b =", a - b)   # letters in a but not in b
print("a | b =", a | b)   # letters in a or b or both
print("a & b =", a & b)   # letters in both a and b
print("a ^ b =", a ^ b)   # letters in a or b but not both

#Similarly to list comprehensions, set comprehensions are also supported:
print("----------------------")
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
