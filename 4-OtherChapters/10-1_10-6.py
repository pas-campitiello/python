import os, glob, sys, re, random, statistics

print()
# Returns an extensive manual page created from the module's docstrings
print(help(str))
print(help(5))

print()
# Return the current working directory
print(os.getcwd())

print()
# Returns a list of all module functions
print(dir(os))

print()
# The glob module provides a function for making file lists from directory wildcard searches
print(glob.glob('*.py'))

print()
# Common utility scripts often need to process command line arguments. 
# These arguments are stored in the sys module’s argv attribute as a list. 
print(sys.argv)

print()
# The re module provides regular expression tools for advanced string processing. 
# For complex matching and manipulation, regular expressions offer succinct, optimized solutions.
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# Removing 1 of 2 consecutive words
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))

print()
print("Randome element from list        :", random.choice(['apple', 'pear', 'banana']))
print("Random list with repetitions     :", [random.choice(range(10)) for _ in range(5)])
print("Random list without repetitions  :", random.sample(range(10), 5))
print("Random number                    :", random.random())
print("Random integer in range(6)       :", random.randrange(6))

print()
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("mean     : ", statistics.mean(data))
print("median   : ", statistics.median(data))
print("variance : ", statistics.variance(data))
