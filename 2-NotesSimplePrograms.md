
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

glob.glob(pathname) - https://docs.python.org/2/library/glob.html
Return a possibly-empty list of path names that match pathname, which must be a string containing a path specification. pathname can be either absolute (like /usr/src/Python-1.5/Makefile) or relative (like ../../Tools/*/*.gif), and can contain shell-style wildcards. Broken symlinks are included in the results (as in the shell).

str. rstrip([chars]) - https://docs.python.org/2/library/stdtypes.html?highlight=rstrip#str.rstrip
Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:

~~~~
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
~~~~


## 11 lines: Triple-quoted strings, while loop 



## 12 lines: Classes 



## 13 lines: Unit testing with unittest 



## 14 lines: Doctest-based testing 



## 15 lines: itertools 



## 16 lines: csv module, tuple unpacking, cmp() built-in 



## 18 lines: 8-Queens Problem (recursion) 



## 20 lines: Prime numbers sieve w/fancy generators 



## 21 lines: XML/HTML parsing (using Python 2.5 or third-party library) 



## 28 lines: 8-Queens Problem (define your own exceptions) 



## 33 lines: "Guess the Number" Game (edited) from http://inventwithpython.com 


