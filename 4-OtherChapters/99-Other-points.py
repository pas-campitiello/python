# https://www.stavros.io/tutorials/python/

# Strings
# WARNING: Watch out for the trailing s in "%(key)s".
print("This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"})

# Exceptions
print("-------------------")

def some_function():
    try:
        # Division by zero raises an exception
        10 / 0
    except ZeroDivisionError:
        print("Oops, invalid.")
    else:
        # Exception didn't occur, we're good.
        pass
    finally:
        # This is executed after the code block is run
        # and all exceptions have been handled, even
        # if a new exception is raised while handling.
        print("We're done with that.")

some_function()

# File I/O
# Python has a wide array of libraries built in. As an example, here is how serializing 
# (converting data structures to strings using the pickle library https://docs.python.org/3.1/library/pickle.html):
print("-------------------")

import pickle
mylist = ["This", "is", 4, 13327]
# Open the file C:\\binary.dat for writing. The letter r before the
# filename string is used to prevent backslash escaping.
myfile = open(r"binary.dat", "wb")
pickle.dump(mylist, myfile)
myfile.close()

myfile = open(r"text.txt", "w")
myfile.write("This is a sample string")
myfile.close()

myfile = open(r"text.txt")
print(myfile.read())
myfile.close()

# Open the file for reading.
myfile = open(r"binary.dat", "rb")
loadedlist = pickle.load(myfile)
myfile.close()
print(loadedlist)

# List comprehensions
print("-------------------")

# Check if a condition is true for any items. 
# "any" returns true if any item in the list is true.
# Consider that 4 % 3 = 1, and 1 is true
print(any([i % 3 for i in [3, 3, 4, 4, 3]]))

# Check for how many items a condition is true.
print(sum(1 for i in [3, 3, 4, 4, 3] if i == 4))
