print("^1".rjust(2), "^2".rjust(3), "^3".rjust(4))
print("------------------------------")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

print()

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
print()
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!a}.'.format(contents))
print('My hovercraft is full of {!s}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making tables pretty.
print()
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
