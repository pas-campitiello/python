
# Notes learning Python

## Python versions

Easy and quick list from Wikipedia (https://en.wikipedia.org/wiki/History_of_Python):

Python 1.0 - January 1994  
Python 1.5 - December 31, 1997  
Python 1.6 - September 5, 2000  

Python 2.0 - October 16, 2000  
Python 2.1 - April 17, 2001  
Python 2.2 - December 21, 2001  
Python 2.3 - July 29, 2003  
Python 2.4 - November 30, 2004  
Python 2.5 - September 19, 2006  
Python 2.6 - October 1, 2008  
Python 2.7 - July 3, 2010  

Python 3.0 - December 3, 2008  
Python 3.1 - June 27, 2009  
Python 3.2 - February 20, 2011  
Python 3.3 - September 29, 2012  
Python 3.4 - March 16, 2014  
Python 3.5 - September 13, 2015  
Python 3.6 - December 23, 2016  

Old releases and dates are listed here: https://www.python.org/download/releases/  
New releases and dates are listed here: https://www.python.org/downloads/

## Python 2+ or Python 3+?

Which is the most important version to use or to start with?  
After some readings online about Python usage, especially 

- https://wiki.python.org/moin/Python2orPython3
- https://www.quora.com/Is-it-better-to-use-Python-2-or-3-in-2016
- https://hynek.me/articles/python3-2016/
- http://ianozsvald.com/2016/06/20/results-for-which-version-of-python-2vs3-do-london-data-scientists-use/

my feeling is that there is not a precise answer to the question, yet.  
It depends mainly on dependencies with old codebases / libraries,  
or deployment environments supporting only old versions of the language.

Python 3+ is the future for sure, but currently (Feb 2017) these seem to be the general rules:

- if you are a beginner, learning Python at school or by yourself, then use Python 3+
- if you are going to start a fresh new project with the latest technologies, then use Python 3+
- if you are going to start a fresh new project using old libraries supporting only Python 2+, hence alternatively
  - you can use Python 2+
  - you can try use Python 3+ and cope with possible backward compatibility 
- if you will deploy your code in an environment supporting only Python 2+, then use Python 2+ 
  - in case you decide to use Python 3+, it can be tricky to cope with backward compatibility, but not impossible
- in all the other cases use Python 2+

I'm in the first condition, beginner, new learner, then I will use Python 3.6.

## Main differences between Python 2+ and 3+

Whatever is the version you choose, it's important to know major differences.  
Some useful links about this topic:

- https://docs.python.org/3/whatsnew/3.0.html
- https://docs.python.org/3/whatsnew/3.6.html
- http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html

## How to install Python 2.* and 3.* on Ubuntu

In Ubuntu 17.04, Python 2.7.13 and Python 3.5.3 are already pre-installed

~~~~
pasq@pas:~/$ python
Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
[GCC 6.3.0 20170118] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
pasq@pas:~/$ python3
Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170118] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~~

## How to execute Python code from command line

Method 1) Using the Python interpreter:  
type each line of code one by one, or on one single line separated by ";" and press Enter.

Method 2) Creating a file .py, for example Tests.py, and running it through the command line with: python Tests.py 

Method 3) Using a [Python IDE](https://www.google.com.au/search?q=python+ide) or an [online IDE](https://www.google.com.au/search?q=python+online+ide).

