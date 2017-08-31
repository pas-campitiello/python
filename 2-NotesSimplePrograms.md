
# Notes on Simple Programs (Python 2.x)
https://wiki.python.org/moin/SimplePrograms


## 2 lines: Input, assignment 

Python 2:
~~~~
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
~~~~

Python 3:
~~~~
name = input('What is your name?\n')
print('Hi, %s.' % name)
~~~~


## 6 lines: Import, regular expressions 

Python re library for regular expression operations: https://docs.python.org/2/library/re.html

~~~~
r'^\d{3}-\d{4}$'
~~~~

**r**  
Indicates Python’s raw string notation (in this case if it is removed there are no effects).

See here: https://stackoverflow.com/questions/21104476/what-does-the-r-in-pythons-re-compiler-pattern-flags-mean

Normal strings use the backslash character as an escape character for special characters (like newlines):
~~~~
>>> print 'this is \n a test'
this is 
 a test
~~~~

The r prefix tells the interpreter not to do this:
~~~~
>>> print r'this is \n a test'
this is \n a test
~~~~

**$**  
Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline.


## 9 lines: Opening files 

**glob.glob(pathname)** - https://docs.python.org/2/library/glob.html
Return a possibly-empty list of path names that match pathname, which must be a string containing a path specification. pathname can be either absolute (like /usr/src/Python-1.5/Makefile) or relative (like ../../Tools/*/*.gif), and can contain shell-style wildcards. Broken symlinks are included in the results (as in the shell).

**str. rstrip([chars])** - https://docs.python.org/2/library/stdtypes.html?highlight=rstrip#str.rstrip
Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:

~~~~
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
~~~~


## 11 lines: Triple-quoted strings, while loop 

For Python 3 just add parenthesis:
~~~~
    print( REFRAIN % (bottles_of_beer, bottles_of_beer,
        bottles_of_beer - 1))
~~~~


## 13 lines: Unit testing with unittest 


Python 2:
~~~~
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
~~~~

Python 3:
- use // for integer division because list indices must be integers or slices, not float.
- user assertEqual instead of failUnlessEqual
~~~~
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
~~~~


## 14 lines: Doctest-based testing 

For Python 3 just use // for integer division because list indices must be integers or slices, not float.  
How does doctest work?  
https://docs.python.org/2/library/doctest.html?highlight=doctest#how-are-docstring-examples-recognized


## 15 lines: itertools 

For Python 3 just add parenthesis where needed in the print functions.

General link: https://stackoverflow.com/questions/20986463/multi-variable-for-loops-python

**str.splitlines()** - http://python-reference.readthedocs.io/en/latest/docs/str/splitlines.html  
Returns a list of the lines in the string, breaking at line boundaries.

**for statement**  
Tutorial control flow: https://docs.python.org/2/tutorial/controlflow.html#for-statements  
Reference: https://docs.python.org/2/reference/compound_stmts.html#for  

~~~~
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
~~~~

**bool([x])** - https://docs.python.org/2/library/functions.html#bool  
If there is an argument x, then it is converted using the standard truth testing procedure. If x is false or omitted, this returns False; otherwise it returns True. Without arguments it returns False:
 bool('') = False  
 bool('fasda') = True

**itertools.groupby** - https://docs.python.org/2/library/itertools.html#itertools.groupby  
The operation of groupby() is similar to the uniq filter in Unix. It generates a break or new group every time the value of the key function changes (which is why it is usually necessary to have sorted the data using the same key function). That behavior differs from SQL’s GROUP BY which aggregates common elements regardless of their input order.  

**str.join(iterable)** - http://python-reference.readthedocs.io/en/latest/docs/str/join.html?highlight=join
Returns a string made from the elements of an iterable, split by [str].
  
This line:
~~~~
groupby(lines, bool):
~~~~
means: apply bool() to the each element of the list lines and generate a new iterable group, basically another list (key = what is returned by bool, value = iterable group) every time bool() changes.  
Therefore it will generate something similar to:
(False, [''])  
(True, ['This is the','first paragraph.'])  
(False, [''])  
(True, ['This is the second.'])  
  
This line:
~~~~
for has_chars, frags in groupby(lines, bool):
~~~~
means: run a for loop on the list of groups created and use the variables *has_chars* and *frags* to refer to the current key and current iterable group.



The output is more comprehensible if you run this:
~~~~
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
~~~~  


## 16 lines: csv module, tuple unpacking, cmp() built-in 



## 18 lines: 8-Queens Problem (recursion) 



## 20 lines: Prime numbers sieve w/fancy generators 



## 21 lines: XML/HTML parsing (using Python 2.5 or third-party library) 



## 28 lines: 8-Queens Problem (define your own exceptions) 



## 33 lines: "Guess the Number" Game (edited) from http://inventwithpython.com 


