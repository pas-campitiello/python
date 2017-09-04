
# Notes on Simple Programs (Python 2.x)
https://wiki.python.org/moin/SimplePrograms


## 2 lines: Input, assignment 

Python 2:
```python
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
```

Python 3:
```python
name = input('What is your name?\n')
print('Hi, %s.' % name)
```


## 6 lines: Import, regular expressions 

Python re library for regular expression operations: https://docs.python.org/2/library/re.html

~~~~
r'^\d{3}-\d{4}$'
~~~~

**r**  
Indicates Python’s raw string notation (in this case if it is removed there are no effects).

See here: https://stackoverflow.com/questions/21104476/what-does-the-r-in-pythons-re-compiler-pattern-flags-mean

Normal strings use the backslash character as an escape character for special characters (like newlines):
```bash
>>> print 'this is \n a test'
this is 
 a test
```

The r prefix tells the interpreter not to do this:
```bash
>>> print r'this is \n a test'
this is \n a test
```

**$**  
Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline.


## 9 lines: Opening files 

**glob.glob(pathname)** - https://docs.python.org/2/library/glob.html
Return a possibly-empty list of path names that match pathname, which must be a string containing a path specification. pathname can be either absolute (like /usr/src/Python-1.5/Makefile) or relative (like ../../Tools/*/*.gif), and can contain shell-style wildcards. Broken symlinks are included in the results (as in the shell).

**str. rstrip([chars])** - https://docs.python.org/2/library/stdtypes.html?highlight=rstrip#str.rstrip
Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:

```python
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
```


## 11 lines: Triple-quoted strings, while loop 

For Python 3 just add parenthesis:
```python
    print( REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
```


## 13 lines: Unit testing with unittest 


Python 2:
```python
import unittest
def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[(size - 1) / 2]
    else:
        return (copy[size/2 - 1] + copy[size/2]) / 2
class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
if __name__ == '__main__':
    unittest.main()
```

Python 3:
- use // for integer division because list indices must be integers or slices, not float.
- user assertEqual instead of failUnlessEqual
```python
import unittest
def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[(size - 1) // 2]
    else:
        return (copy[size//2 - 1] + copy[size//2]) / 2
class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
if __name__ == '__main__':
    unittest.main()
```


## 14 lines: Doctest-based testing 

For Python 3 just use // for integer division because list indices must be integers or slices, not float.  
How does doctest work?  
https://docs.python.org/2/library/doctest.html?highlight=doctest#how-are-docstring-examples-recognized


## 15 lines: itertools 

For Python 3 just add parenthesis where needed in the print functions.

**str.splitlines()** - http://python-reference.readthedocs.io/en/latest/docs/str/splitlines.html  
Returns a list of the lines in the string, breaking at line boundaries.

**for statement**  
Tutorial control flow: https://docs.python.org/2/tutorial/controlflow.html#for-statements  
Reference: https://docs.python.org/2/reference/compound_stmts.html#for  

```python
# Given a matrix or a map, you can cycle through it by lines (using only 1 index) 
# or by columns (using a number of indexes equal to the number of columns per row)

list1 = [('a', 'b', 123), ('d', 'e', 234), ('d', 'e', 234)]
list2 = [('z', 'w', 999), ('y', 'h', 666)]

for i in list1:
   print i
print

for i in list2:
   print i
print

#for i,j in list1:
#    print i,',', j
#print

#for i,j in list2:
#    print i,',', j
#print

for i,j,k in list1:
    print i,',', j,',', k
print

for i,j,k in list2:
    print i,',', j,',', k
print
```

**bool([x])** - https://docs.python.org/2/library/functions.html#bool  
If there is an argument x, then it is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise it returns True. Without arguments it returns False:
 bool('') = False  
 bool('fasda') = True

**itertools.groupby** - https://docs.python.org/2/library/itertools.html#itertools.groupby  
The operation of groupby() is similar to the uniq filter in Unix. It generates a break or new group every time the value of the key function changes (which is why it is usually necessary to have sorted the data using the same key function). That behavior differs from SQL’s GROUP BY which aggregates common elements regardless of their input order.  

**str.join(iterable)** - http://python-reference.readthedocs.io/en/latest/docs/str/join.html?highlight=join  
Returns a string made from the elements of an iterable, split by [str].
  
This line
```python
groupby(lines, bool):
```
means: apply bool() to the each element of the list lines and generate a new iterable group, basically another list (key = what is returned by bool, value = iterable group) every time bool() changes.  
Therefore it will generate something similar to:  
```
(False, [''])  
(True, ['This is the','first paragraph.'])  
(False, [''])  
(True, ['This is the second.'])  
```

This line
```python
for has_chars, frags in groupby(lines, bool):
```
means: run a for loop on the list of groups created and use the variables *has_chars* and *frags* to refer to the current key and current iterable group.



The output is more comprehensible if you run this:
```python
from itertools import groupby
lines = '''
This is the
first paragraph.

This is the second.
'''.splitlines()

print lines
print
for i in groupby(lines, bool):
   print i
print
# Use itertools.groupby and bool to return groups of
# consecutive lines that either have content or don't.
for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print ' '.join(frags)
# PRINTS:
# This is the first paragraph.
# This is the second.
```  

## 16 lines: csv module, tuple unpacking, cmp() built-in 

**csv library** - https://docs.python.org/2/library/csv.html?highlight=csv#module-csv  
**open** - https://docs.python.org/3/library/functions.html#open  

**cmp** - https://docs.python.org/2/library/functions.html?highlight=cmp#cmp  
cmp(x, y): compares the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y.
   
This line
```python
cmp(float(change), 0.0)
```
means: compare the float version of change with 0.0
- if float(change) < 0.0, then return a negative value (-1) 
- if float(change) == 0.0, then return 0
- if float(change) < 0.0, then return a positive value (1).

## 18 lines: 8-Queens Problem (recursion) 

https://en.wikipedia.org/wiki/Eight_queens_puzzle
The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other.

The program prints out all the solutions to the problem five an initial BOARD_SIZE.

**reversed(seq)** - https://docs.python.org/2/library/functions.html?highlight=reversed#reversed  
Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

**range(start, stop[, step])** - https://docs.python.org/2/library/functions.html#range
This is a versatile function to create lists containing arithmetic progressions:
```bash
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)
[0, 3, 6, 9]
>>> range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
```

**xrange(start, stop[, step])** - https://docs.python.org/2/library/functions.html#xrange  
This function is very similar to range(), but returns an xrange object instead of a list.   

The xrange type is an immutable sequence which is commonly used for looping. The advantage of the xrange type is that an xrange object will always take the same amount of memory, no matter the size of the range it represents. There are no consistent performance advantages.  

The xrange type is an opaque sequence type which yields the same values as the corresponding list, without actually storing them all simultaneously. The advantage of xrange() over range() is minimal (since xrange() still has to create the values when asked for them) except when a very large range is used on a memory-starved machine or when all of the range’s elements are never used (such as when the loop is usually terminated with break).

This part of the code
```python
    return [solution+[(n,i+1)]
        for i in xrange(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)]
```
means: return the list of the sums between solution+[(n,i+1)] generated with the 2 for loops.

## 20 lines: Prime numbers sieve w/fancy generators 

**itertools.count(start=0, step=1)** - https://docs.python.org/2/library/itertools.html#itertools.count  
Make an iterator that returns evenly spaced values starting with n. 
Equivalent to:
```python
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
```

**yield** - For an explanation about see here: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do  
**yield** is a keyword that is used like *return*, except the function will return a generator [and it does not exit from the current block of code]. [...] it's handy when you know your function will return a huge set of values that you will only need to read once.

**__rmod__()**  
This code
```python
prime = 7
print prime.__rmod__(88)
```
returns 4 (= 88 mod 7).

**itertools.ifilter(predicate, iterable)** - https://docs.python.org/2/library/itertools.html#itertools.ifilter  
Make an iterator that filters elements from iterable returning only those for which the predicate is **True** or **1**. If predicate is None, return the items that are true. 

These lines
```python
prime = numbers.next()
yield prime
numbers = itertools.ifilter(prime.__rmod__, numbers)
```
mean: 
- take the next number in the initial iterator *numbers*
- create a generator object, return it and continue
- then each number x in numbers, perform x mod prime  
-- if the result is 0, then yield x  
-- if the result is not 0, then do not yield or return anything  
-- the x returned will form an iterator of generators (if you print it you loose it) stored again in *numbers*.  
-- in this way after the first loop numbers will contain all the numbers not divisible by 2, then those not divisible by 2 and 3, then those not divisible by 2,3,5, and so on, therefore numbers.next() will always give the next prime number in the iteration.

For Python 3 version see here: https://github.com/python/mypy/issues/1227  

```python
import itertools
from typing import Iterator

def iter_primes() -> Iterator[int]:
    numbers = itertools.count(2)
    while True:
        prime = next(numbers)
        yield prime

        numbers = filter(prime.__rmod__, numbers)

for p in iter_primes():
    if p > 1000:
        break
    print(p)
```

## 21 lines: XML/HTML parsing (using Python 2.5 or third-party library) 



## 28 lines: 8-Queens Problem (define your own exceptions) 



## 33 lines: "Guess the Number" Game (edited) from http://inventwithpython.com 


