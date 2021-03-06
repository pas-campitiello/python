# 4 - Other important things from the official tutorial
Official tutorial: https://docs.python.org/3/tutorial/index.html


## 4.7.5 Lambda expressions
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Probably the most useful way to exploit lambda functions is define them in-line and/or in small function as an argument:

```python
# It sorts the list of pairs using as key the second value of each pair.

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# It creates a list of squares until 10
print(list(map(lambda x: x**2, range(10))))
```

**list.sort()** - https://docs.python.org/3/library/stdtypes.html#list.sort  

Key specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used for the entire sorting process. The default value of None means that list items are sorted directly without calculating a separate key value.

**map(function, iterable, …)** - https://docs.python.org/3/library/functions.html#map  
Return an iterator that applies function to every item of iterable, yielding the results. 


## 5.1.3. List Comprehensions
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

```python
print([x**2 for x in range(10)])

print("--------------------")

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

print("--------------------")

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

print("--------------------")

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
```

## 5.1.4. Nested List Comprehensions
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions

``` python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = []

print([row[3] for row in matrix])

for i in range(4):
    transposed.append([row[i] for row in matrix])

print("Matrix:     ", matrix)
print("Transposed: ", transposed)

print("----------------------")

transposedAgain = []
for i in range(3):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in transposed:
        transposed_row.append(row[i])
    transposedAgain.append(transposed_row)

print("Transposed again: ", transposedAgain)

print("----------------------")
print("Transposed using zip(): ", list(zip(*matrix)))
```

**zip(\*iterables)**  
https://docs.python.org/3/library/functions.html#zip

Make an iterator that aggregates elements from each of the iterables.
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.


## 5.4 Sets
https://docs.python.org/3/tutorial/datastructures.html#sets

``` python
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
```

## 5.5 Dictionaries
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 

It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary.

``` python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print("---------------------------------")

print(list(tel.keys()))
print(sorted(tel.keys()))

print("'guido' in tel? -", 'guido' in tel)
print("'jack' not in tel? -", 'jack' not in tel)

print("---------------------------------")

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
print({x: x**2 for x in (2, 4, 6)})

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
print(dict(sape=4139, guido=4127, jack=4098))
```

## 5.6 Looping techniques
https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

**items()** - https://docs.python.org/3/library/stdtypes.html#dict.items
Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.

**enumerate(iterable, start=0)** - https://docs.python.org/3/library/functions.html#enumerate
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The \_\_next\_\_() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

``` python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print("--------------------------------------------------")
for i, v in enumerate(['tic', 'tac', 'toe']):
     print(i, v)

print("--------------------------------------------------")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))

print("--------------------------------------------------")

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
     if not math.isnan(value):
         filtered_data.append(value)
print(filtered_data)
```

## 5.8. Comparing Sequences and Other Types
https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types

The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively.

Comparison is performed in couples, if the items in a couple differ the comparison stops immediately and there is an outcome.

``` python
print("(1, 2, 4)                < (1, 2, 4)               ?", (1, 2, 4) < (1, 2, 4))
print("[1, 2, 3]                < [1, 2, 4]               ?", [1, 2, 3] < [1, 2, 4])
print("[9, 2, 3]                < [1, 2, 4]               ?", [9, 2, 3] < [1, 2, 4])
print("(1, 2, 3)                == (1.0, 2.0, 3.0)        ?", (1, 2, 3) == (1.0, 2.0, 3.0))
print()
print("'ABC' < 'C' < 'Pascal'   < 'Python'                ?", 'ABC' < 'C' < 'Pascal' < 'Python')                 # alphabetical order
print()
# Comparison is performed in couples, if the items in a couple differ the comparisnn stops immediately and there is an outcome.
print("(1, 2, 3, 4)             < (1, 2, 4)               ?", (1, 2, 3, 4) < (1, 2, 4))                          # problem here
print()
# If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one.")
print("(1, 2)                   < (1, 2, -1)              ?", (1, 2) < (1, 2, -1))
print()
print("('aa')                   < ('abc')                 ?", ('aa') < ('abc'))
print("('aa', 'ab')             < ('abc', 'a')            ?", ('aa', 'ab') < ('abc', 'a'))
print()
print("(1, 2, ('aa', 'ab'))     < (1, 2, ('abc', 'a'), 4) ?", (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
```

## 6.3. The dir() Function
https://docs.python.org/3/tutorial/modules.html#the-dir-function
https://docs.python.org/3/library/functions.html#dir

The built-in function **dir()** is used to find out which names a module defines. It returns a sorted list of strings.

Without arguments, **dir()** lists the names you have defined currently.

**dir()** does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module _builtins_.

```python
import time, builtins
print(dir(time))
print()
print(dir())
print()
print(dir(builtins))
```

## 7.1 Fancier Output Formatting
https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting

```python
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
```

## 7.2.2. Saving structured data with json
https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json
https://docs.python.org/3/library/json.html#module-json

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called _serializing_. Reconstructing the data from the string representation is called _deserializing_. 

```python
import json

x = [1, 'simple', 'list', ('aa','bb')]
print(json.dumps(x))

f = open("contentfile.txt", "w")
# note json.dump not dumps
json.dump(x,f)
f.close()

f = open("contentfile.txt", "r")
readContent = json.load(f)
f.close()

print(readContent)
```


## 9.3 A first look at classes
https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

Compared with other programming languages, Python’s class mechanism adds classes with a minimum of new syntax and semantics. It is a mixture of the class mechanisms found in C++ and Modula-3. Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

The simplest form of class definition looks like this:
```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Example:
```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r,"+ (", x.i,")*i")
```

## 9.5 Inheritance
https://docs.python.org/3/tutorial/classes.html#inheritance

The syntax for a derived class definition looks like this:
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
The name BaseClassName must be defined in a scope containing the derived class definition.

Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

## 9.6 Private variables
https://docs.python.org/3/tutorial/classes.html#private-variables

“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. \_spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form **\_\_spam** (at least two leading underscores, at most one trailing underscore) is textually replaced with **\_classname\_\_spam**, where **classname** is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

## 9.8 Iterators
https://docs.python.org/3/tutorial/classes.html#iterators  
https://docs.python.org/3/library/functions.html#iter

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(rev.__doc__)

print()
print(rev)
iterator = iter(rev)
print(iterator)

print()

for char in rev:
    print(char)
```

## 9.9 Generators
https://docs.python.org/3/tutorial/classes.html#generators  

Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the **yield** statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the **\_\_iter\_\_()** and **\_\_next\_\_()** methods are created automatically.

Another key feature is that the local variables and execution state are automatically saved between calls. This made the function easier to write and much more clear than an approach using instance variables like self.index and self.data.

In addition to automatic method creation and saving program state, when generators terminate, they automatically raise StopIteration. In combination, these features make it easy to create iterators with no more effort than writing a regular function.

**generator** - https://docs.python.org/3/glossary.html#term-generator

A function which returns a generator iterator. It looks like a normal function except that it contains **yield** expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the **next()** function.
Usually refers to a generator function, but may refer to a generator iterator in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
     print(char)
```

## 10. Brief Tour of the Standard Library
https://docs.python.org/3/tutorial/stdlib.html

```python
import os, glob, sys, re, random, statistics

print()
# Returns an extensive manual page created from the module's docstrings
print(help(str))

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
```

```python
# There are a number of modules for accessing the internet and processing internet protocols. 
# Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail 

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
     for line in response:
         line = line.decode('utf-8')         # Decoding the binary data to text
         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
             print(line)


print()
# Note that this example needs a mailserver running on localhost, for example Fake SMTP Server
import smtplib
server = smtplib.SMTP('localhost:2525')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    """To: jcaesar@example.org
    From: soothsayer@example.org
    
    Beware the Ides of March.
    """)
server.quit()


print()
# Dates are easily constructed and formatted
from datetime import date
now = date.today()
print("Now: ", now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1986, 6, 30)
age = now - birthday
print(age.days)
```

```python
# Common data archiving and compression formats are directly supported 
# by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))


print()
# Python provides a measurement tool that answers those questions immediately.
# For example, it may be tempting to use the tuple packing and unpacking feature 
# instead of the traditional approach to swapping arguments. 
# The timeit module quickly demonstrates a modest performance advantage:
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())


print()
# The doctest module provides a tool for scanning a module 
# and validating tests embedded in a program’s docstrings. 
# Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. 

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests, it prints nothing if test passes

print()
# The unittest module is not as effortless as the doctest module, 
# but it allows a more comprehensive set of tests to be maintained in a separate file:

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```


## 11. Brief Tour of the Standard Library II
https://docs.python.org/3/tutorial/stdlib2.html

```python
# The locale module accesses a database of culture specific data formats. 
# The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators:

import locale

print(locale.locale_alias)
print()
# print(locale.setlocale(locale.LC_ALL, 'english_united-states.437'))
print(locale.setlocale(locale.LC_ALL, 'en_US.utf8'))
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
```

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

```python
# The bisect module contains functions for manipulating sorted lists
import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

# The heapq module provides functions for implementing heaps based on regular lists. 
# The lowest valued entry is always kept at position zero. 
# This is useful for applications which repeatedly access the smallest element 
# but do not want to run a full list sort 
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                               # rearrange the list into heap order
heappush(data, -5)                          # add a new entry
print([heappop(data) for i in range(3)])    # fetch the three smallest entries
```

```python
# The decimal module offers a Decimal datatype for decimal floating point arithmetic.
from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))

# The Decimal result keeps a trailing zero, 
# automatically inferring four place significance from multiplicands with two place significance. 
# Decimal reproduces mathematics as done by hand and avoids issues that can arise 
# when binary floating point cannot exactly represent decimal quantities.

# Exact representation enables the Decimal class to perform modulo calculations 
# and equality tests that are unsuitable for binary floating point
print()
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)

print()
print(sum([Decimal('0.1')]*10), " = Decimal('1.0') ?", sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10), " = 1.0 ?", sum([0.1]*10)  == 1.0)

#The decimal module provides arithmetic with as much precision as needed:
print()
getcontext().prec = 36
print(Decimal(1) / Decimal(7))
```

## 12. Virtual Environments and Packages
https://docs.python.org/3/tutorial/venv.html

You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from the Python Package Index, <https://pypi.python.org/pypi>. You can browse the Python Package Index by going to it in your web browser, or you can use pip’s limited search feature:

```bash
(tutorial-env) $ sudo apt install pip

...

(tutorial-env) $ pip search astronomy
skyfield               - Elegant astronomy for Python
gary                   - Galactic astronomy and gravitational dynamics.
novas                  - The United States Naval Observatory NOVAS astronomy library
astroobs               - Provides astronomy ephemeris to plan telescope observations
PyAstronomy            - A collection of astronomy related tools for Python.
...
```

You can install the latest version of a package by specifying a package’s name:

```bash
(tutorial-env) $ pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

You can also **install** a specific version of a package by giving the package name followed by == and the version number:

```bash
(tutorial-env) $ pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

You can supply a different version number to get that version, or you can run **pip install --upgrade** to upgrade the package to the latest version:

```bash
(tutorial-env) $ pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

**pip uninstall** followed by one or more package names will remove the packages from the virtual environment.  
**pip show** will display information about a particular package.  
**pip list** will display all of the packages installed in the virtual environment:
```bash
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```


## 99. Other points
https://www.stavros.io/tutorials/python/

```python
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
```
