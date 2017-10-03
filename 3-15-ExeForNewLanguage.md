
# 15 exercises for learning Python
Inspired by: http://www.ign.com/boards/threads/15-exercises-for-learning-a-new-programming-language.129542936/


## Exercise 1
Display series of numbers (1,2,3,4, 5....etc) in an infinite loop.  
The program should quit if someone hits a specific key (say ESCAPE key).

Infinite loop printing numbers with 0.5 seconds delay:
```python

import time

i = 0
while True:
    print(i)
    i+=1
    time.sleep(0.5)
```

**curses library** - https://docs.python.org/3/howto/curses.html  

Infinite loop, waiting for ESCape to be pressed to exit:
```python
import curses

def main(stdscr):

    while True:

        c = stdscr.getch()
        if c == 27: # ESC code
            break   # Exit the while loop for ESC

curses.wrapper(main)
```

or with [input](https://docs.python.org/2/library/functions.html#input):
```python
while True:

    c = input("> ")
    if c == "q":    
        break       # Exit the while loop for "q"
```

Mixing the things, it works but the input of a char blocks the loop, for example using both curses and input:
```python
import curses
import time

def main(stdscr):

    i = 0

    while stdscr.getch() != 27:
        print(i)
        i+=1
        time.sleep(0.5)

curses.wrapper(main)


i = 0

while input(">") != "q":
    print(i)
    i+=1
    time.sleep(0.5)
```

Also using a combination of othere libraries the problem is the same, see [here](https://stackoverflow.com/questions/34497323/what-is-the-easiest-way-to-detect-key-presses-in-python-3-on-a-linux-machine).

Reading [here](http://forums.xkcd.com/viewtopic.php?t=99890) I discovered a thread example; modifying it slightly it looks like:
```python
import _thread, time, sys

def input_thread(L):
    input()
    print("aaaaa")    
    
def do_print():
    L = []
    _thread.start_new_thread(input_thread, (L,))
    i = 0    
    while 1:
        if L: break
        time.sleep(1)
        print(i)
        i += 1
       
do_print()
```
but this has another problem in Linux (Ubuntu 17.04): the loop works and it accepts inputs but to verify the input it's necessary to press Enter, and when input_thread(L) returns, the thread [silently exits](https://docs.python.org/3/library/_thread.html#_thread.start_new_thread) and the function is executed only once. Executing the code above: 0 will be printed to the screen, then you have 1 second to type something, press Enter and see "aaaaa". In any case, after the first input the thread with input_thread(L) exits, even if you can input some chars while the numbers are printed, that input is not read or stored anywhere.

There must be a solution simpler than a thread based one. Reading in the same forum I discovered also the function **nodelay()** in curses:
- https://docs.python.org/3/howto/curses.html#user-input
- https://docs.python.org/2/library/curses.html

```python
import curses
import time

def main(stdscr):

    stdscr.nodelay(1)
    i = 0

    while stdscr.getch() != 27:
        print(i)
        i+=1
        time.sleep(0.1)

curses.wrapper(main)
```
Now this is solutions works pretty well except that it prints the numbers with some initial spaces. This is [because](https://docs.python.org/3/howto/curses.html#what-is-curses):  
The curses library provides fairly basic functionality, providing the programmer with an abstraction of a display containing multiple non-overlapping windows of text. 

The library curses creates and returns a special window overlapped to the terminal one, in order to interact with curses window you are supposed to use its internal functions. In this case the function print will not work properly within curses window, the correct function to use is **addstr**, see [here](https://docs.python.org/3/library/curses.html?highlight=addstr#curses.window.addstr).

Therefore this is the solution I was looking for to display a series of numbers (1,2,3,4, 5....etc) in an infinite loop quitting if the user hits the ESCape key:
```python
import curses
import time

def main(win):

    win.nodelay(1)
    i = 0

    while win.getch() != 27:
        win.addstr("{0}\n".format(str(i)))
        i+=1
        time.sleep(0.1)

curses.wrapper(main)
```

## Exercise 2
Fibonacci series, swapping two variables, finding maximum/minimum among a list of numbers.

Fibonacci 1:
```python
import curses
import time

def main(win):

    win.nodelay(1)
    init = 0
    prec = 0    
    next = 1

    while win.getch() != 27:
        win.addstr("{0}\n".format(str(next)))
           
        prec = next     
        next = next + init
        init = prec
        
        time.sleep(0.5)

curses.wrapper(main)
```

Fibonacci 2:
```python
init = 0
prec = 0    
next = 1

while next < 1000:
    prec = next     
    next = next + init
    init = prec
    print(next)
```

I also found a nice function [here](https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python) to print the **n**th Fibonacci number:
```python
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2) 

print(F(10))
```

Another interesting example showing the usage of modules and some implemetations of Fibonacci functions is here: https://docs.python.org/3/tutorial/modules.html

> For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
```

> Now enter the Python interpreter and import this module with the following command:
```python
>>> import fibo
```

> This does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there. Using the module name you can access the functions:
```python
>>> fibo.fib(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

Find maximum and minimum elements in a list is as simple as this (see [built-in functions](https://docs.python.org/2/library/functions.html)):
```python
numlist = [1,14,57,9,40,4,3,2,22,66,88,99,10]
print(max(numlist))
print(min(numlist))
```

Another example:
```python
num = 0
numlist = []
while True:
    num = input("Insert a number or 'q' to quit: ")
    if num=="q": break    
    numlist.append(int(num))

print("List: ",numlist)
print("Max: ",max(numlist))
print("Min: ",min(numlist))
```


## Exercise 3
Accepting series of numbers, strings from keyboard and sorting them ascending, descending order.

See here https://docs.python.org/2/library/functions.html#sorted  
and here https://docs.python.org/2/howto/sorting.html#sortinghowto

```python
numbers = [9, 99, 12, 35, 46, 77]
print("Numbers: ", numbers)
numbers.sort()
print("Numbers sorted: ", numbers)

strings = ['zarea', 'perimeter', 'location']
print("String: ", strings)
strings.sort()
print("String sorted: ",strings)

print("==============")

num = 0
numbers = []
while True:
    num = input("Insert a number or 'q' to quit: ")
    if num=="q": break    
    numbers.append(int(num))

print("List: ",numbers)
print("Sorted ascending : ",sorted(numbers))
print("Sorted descending: ",sorted(numbers, reverse=True))

print("==============")

inp = 0
strings = []
while True:
    inp = input("Insert a string or '999' to quit: ")
    if inp=="999": break    
    strings.append(str(inp))

print("List: ",strings)
print("Sorted ascending : ",sorted(strings))
print("Sorted descending: ",sorted(strings, reverse=True))
```

## Exercise 4
Reynolds number is calculated using formula (D*v*rho)/mu  
Where D = Diameter, V= velocity, rho = density mu = viscosity  
Write a program that will accept all values in appropriate units (Don't worry about unit conversion).  
If number is < 2100, display Laminar flow,  
If it’s between 2100 and 4000 display 'Transient flow' and  
if more than '4000', display 'Turbulent Flow' (If, else, then...).

What are the "appropriate units"?  
According to [Wikipedia](https://en.wikipedia.org/wiki/Reynolds_number), the Reynolds number is defined as  

    Re = ρ u L / μ = u L / ν 

where:  

    ρ is the density of the fluid (SI units: kg/m^3)
    u is the velocity of the fluid with respect to the object (m/s)
    L is a characteristic linear dimension (m)
    μ is the dynamic viscosity of the fluid (Pa·s or N·s/m^2 or kg/m·s)
    ν is the kinematic viscosity of the fluid (m^2/s).

so:

```python
D = float(input("Insert diameter or the characteristic linear dimension in m: "))
v = float(input("Insert the velocity of the fluid with respect to the object in m/s: ")) 
rho = float(input("Insert the density of the fluid in SI units kg/m^3: "))
mu = float(input("Insert the dynamic viscosity of the fluid in Pa·s or N·s/m^2 or kg/m·s: "))

Re = (D*v*rho) / mu  

print(Re)

if (Re <= 2100):
    print("Laminar flow")
elif (Re > 2100 and Re <= 4000):
    print("Transient flow") 
else:
    print("Turbulent Flow")
```

## Exercise 5
Modify the above program such that it will ask for 'Do you want to calculate again (y/n),
if you say 'y', it'll again ask the parameters. If 'n', it'll exit. (Do while loop).

While running the program give value mu = 0. See what happens. Does it give 'DIVIDE BY ZERO' error?
Does it give 'Segmentation fault..core dump?'  
How to handle this situation. Is there something built in the language itself? (Exception Handling).

See here: https://docs.python.org/3/tutorial/errors.html
``` python
again = "y"

while again == "y":

    D = float(input("Insert diameter or the characteristic linear dimension in m: "))
    v = float(input("Insert the velocity of the fluid with respect to the object in m/s: ")) 
    rho = float(input("Insert the density of the fluid in SI units kg/m^3: "))
    mu = float(input("Insert the dynamic viscosity of the fluid in Pa·s or N·s/m^2 or kg/m·s: "))

    try:
        Re = (D*v*rho) / mu  
        
        print(Re)

        if (Re <= 2100):
            print("Laminar flow")
        elif (Re > 2100 and Re <= 4000):
            print("Transient flow") 
        else:
            print("Turbulent Flow")

    except ZeroDivisionError:
        print("Oops! Division by 0!")

    again = input("Do you want to calculate again (y/n)? ")
```


## Exercise 6
Scientific calculator supporting addition, subtraction, multiplication, division, square-root, square, cube,
sin, cos, tan, Factorial, inverse, modulus.

See here:   
1) https://docs.python.org/3/library/math.html
2) https://docs.python.org/3/library/functions.html
3) https://en.wikibooks.org/wiki/Python_Programming/Basic_Math#Mathematical_Operators
4) https://docs.python.org/3.6/library/operator.html#mapping-operators-to-functions

```python
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
```

## Exercise 7
Printing output in different formats (say rounding up to 5 decimal places, truncating after 4 decimal places,
padding zeros to the right and left, right and left justification). (Input output operations)

See here:   
1) https://docs.python.org/3/library/math.html
2) https://docs.python.org/3/library/functions.html
3) https://stackoverflow.com/questions/783897/truncating-floats-in-python
4) https://stackoverflow.com/questions/20544714/truncate-a-decimal-value-in-python
5) https://docs.python.org/3/library/stdtypes.html
6) https://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-string
7) https://docs.python.org/3/library/stdtypes.html#old-string-formatting
8) https://stackoverflow.com/questions/5084743/how-to-print-pretty-string-output-in-python

```python
import operator, math, decimal

def truncateDecimals1(strNum, x):
    posDot = strNum.index(".")
    print(" dot position =", posDot)
    print(" int part .   =", strNum[:posDot+1]) 
    print(" decimal part =", strNum[posDot+1:posDot+x+1])
    return strNum[:posDot+1] + strNum[posDot+1:posDot+x+1]

def truncateDecimals2(strNum, x):
    before_dec, after_dec = str(strNum).split('.')
    return float('.'.join((before_dec, after_dec[0:x])))    

def truncateDecimals3(num):
    return decimal.Decimal(num).quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_DOWN)

def truncateDecimals4(num, x):
    return math.floor(num * 10**x) / 10**x

print("---- rounding up to 5 decimal places ----\n")

num = float(input("Insert a float number: "))

print("math.ceil(num) =", math.ceil(num))
print("round(num)     =", round(num))
print("round(num,4))  =", round(num,4) )
print("round(num,5))  =", round(num,5) )
print("'%.5f' % num   =", "%.5f" % num )
print("math.pi        =", math.pi )
print("'%5.3f' % num  =", "%5.3f" % math.pi )

print("\n---- truncating after 4 decimal places ----\n")
print("math.trunc(num)                  =", math.trunc(num))
print("str(num)[:6]                     =", str(num)[:6])
print("truncateAtDecimals1(str(num),4)) =", float(truncateDecimals1(str(num),4)))
print("truncateAtDecimals2(str(num),4)) =", truncateDecimals2(str(num),4))
print("truncateAtDecimals3(num))        =", truncateDecimals3(num))
print("truncateAtDecimals4(num,4))      =", truncateDecimals4(num,4))

print("\n---- padding zeros to the right and left ----\n")
print("str(num).zfill(5)        =", str(num).zfill(5))
print("'-42'.zfill(5)           =", "-42".zfill(5))
print("str(num).center(20,'0')  =", str(num).center(20,"0"))
print("str(num).rjust(20,'0')   =", str(num).rjust(20,"0"))
print("str(num).ljust(20,'0')   =", str(num).ljust(20,"0"))
print("'{0:03f}'.format(num)    =",'{0:03f}'.format(num))
print('%(thisword)s is this one %(number)05f with 5 padding zeros right.' % {'thisword': "Your number", "number": num})
print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})

print("\n---- right and left justification ----\n")
print("str(num).rjust(20,' ')   =", ">", str(num).rjust(20," "), "<")
print("str(num).ljust(20,' ')   =", ">", str(num).ljust(20," "), "<")
```

## Exercise 8
Open a text file and convert it into HTML file. (File operations / Strings)

See here:
1) https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
2) https://stackoverflow.com/questions/28873349/python-readlines-not-returning-anything
3) https://stackoverflow.com/questions/10507230/insert-line-at-middle-of-file-with-python
4) https://docs.python.org/3/library/stdtypes.html#list
5) https://docs.python.org/3/library/os.html

Example 1, list and read files:
```python
import os

print("----- list files in a folder -----\n")

print("Files in the current folder:\n", os.listdir())
print("\nFiles in the root folder:\n", os.listdir('/'))

print("\n----- read and print content of a file -----\n")

f = open('contentfile.txt')
print ("Name of the file: ", f.name)
for line in f:
    print(line, end='')

with open('contentfile.txt') as f:
    read_data = f.read()
    print ("File content again:")
    print(read_data)

f2 = open('../1-VersionsAndSetup.md')
print ("Name of the file: ", f2.name)
line = f2.readlines()
print ("Read lines: %s" % (line))

f2.close()
```

Example 2, modify existing and create new file:
```python
print("\n----- modify the content of an existing file -----\n")

f = open("contentfile.txt", "r")
contents = f.readlines()
f.close()

print(contents)
contents.insert(2, "New line in the middle of the content file\n")

f = open("contentfile.txt", "w")
contents = "".join(contents)
f.write(contents)
f.close()

print()
f = open('contentfile.txt')
for line in f:
    print(line, end='')


with open('contentfile.txt', 'a') as f3:
    f3.write("New line appended at the end of the content file.\n")
    
with open('contentfile.txt') as f3:
    read_data = f3.read()
    print ("File content again:")
    print(read_data)

print("\n----- create a new file -----\n")

f = open("contentfile2.txt", "w")
contents = f.write("Content in the new file\n")
f.close()

with open('contentfile.txt') as f3:
    read_data = f3.read()
    print ("File content:")
    print(read_data)
```

Example 3, rename and delete file:
```python
import os

print("\n----- rename a file -----\n")

os.rename("contentfile2.txt", "new_name_contentfile2.htm")

with open('new_name_contentfile2.htm') as f3:
    read_data = f3.read()
    print ("File content again:")
    print(read_data)

try:
    with open('contentfile2.txt') as f3:
        read_data = f3.read()
        print ("File content:")
        print(read_data)
except FileNotFoundError:
    print("File named contentfile2.txt not found!")

print("\n----- delete a file in a folder -----\n")

os.remove("new_name_contentfile2.htm")

try:
    with open('new_name_contentfile2.htm') as f3:
        read_data = f3.read()
        print ("File content:")
        print(read_data)
except FileNotFoundError:
    print("File named new_name_contentfile2.htm not found!")
```

## Exercise 9
Time and Date: get system time and convert it in different formats 'DD-MON-YYYY', 'mm-dd-yyyy', 'dd/mm/yy' etc.

See here:
1) https://docs.python.org/3/library/datetime.html
2) https://docs.python.org/3/library/time.html
3) https://pymotw.com/3/datetime/

```python
import datetime, time

print("datetime.date                =", datetime.date)
print("datetime.time                =", datetime.time)
print()
print("datetime.date.today()        =", datetime.date.today())
print("datetime.date.today().year   =", datetime.date.today().year)
print("datetime.date.today().month  =", datetime.date.today().month)
print("datetime.date.today().day    =", datetime.date.today().day)
print()
print("datetime.datetime.now()                  =", datetime.datetime.now())
print("datetime.datetime.today()                =", datetime.datetime.today())
print("datetime.datetime.today().hour           =", datetime.datetime.today().hour)
print("datetime.datetime.today().minute         =", datetime.datetime.today().minute)
print("datetime.datetime.today().second         =", datetime.datetime.today().second)
print("datetime.datetime.today().microsecond    =", datetime.datetime.today().microsecond)
print("datetime.datetime.today().weekday()      =", datetime.datetime.today().weekday())
print("datetime.datetime.today().isoweekday()   =", datetime.datetime.today().isoweekday())
print("datetime.datetime.today().timetz()       =", datetime.datetime.today().timetz())
print()
print("time.ctime() =", time.ctime())
print()
timenow = datetime.datetime.now()
print("%Y-%m-%d_%H:%M:%S    =", timenow.strftime('%Y-%m-%d_%H:%M:%S'))
print("%D                   =", timenow.strftime('%D'))
print("%m-%d-%y             =", timenow.strftime('%m-%d-%y'))
print("%a %d/%m/%y          =", timenow.strftime('%a %d/%m/%y'))
print("%A %d/%m/%y          =", timenow.strftime('%A %d/%m/%y'))
print()
print("%A %b %d/%m/%y - %H:%M:%S    =", timenow.strftime('%A %b %d/%m/%y - %H:%M:%S'))
print("%a %B %d - %H:%M             =", timenow.strftime('%a %B %d - %H:%M'))
print("%d-%B-%Y                     =", timenow.strftime('%d-%B-%Y'))
print("%m-%d-%Y                     =", timenow.strftime('%m-%d-%Y'))
print("%d/%m/%Y                     =", timenow.strftime('%d/%m/%Y'))
```

## Exercise 10
Create files with date and time stamp appended to the name.

```python
import datetime

timenow = datetime.datetime.now()
timestamp = timenow.strftime('%Y%m%d%H%M')
print(timestamp)

name = ()

f = open("contentfile-" + timestamp + ".txt", "w")
contents = f.write("Content in the new file with this timestamp " + timestamp)
f.close()
```

## Exercise 11
Input is HTML table, remove all tags and put data in a comma / tab separated file.

[Here](https://wiki.python.org/moin/SimplePrograms) there was already the 21 lines example with Python 2 that was doing a similar thing.  
Adapting that example, this is a solution to exercise 11:

```python
dinner_recipe = '''<html><body><table>
<tr><th>amt</th><th>unit</th><th>item</th></tr>
<tr><td>24</td><td>slices</td><td>baguette</td></tr>
<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
<tr><td>1</td><td>jar</td><td>pesto</td></tr>
</table></body></html>'''

import xml.etree.ElementTree as etree
tree = etree.fromstring(dinner_recipe)

f = open("table.csv", "w")

for amt, unit, item in tree.getiterator('tr'):
    print("%s,%s,%s" % (amt.text, unit.text, item.text))
    f.write("%s,%s,%s\n" % (amt.text, unit.text, item.text))

f.close()
```

Reading the HTML code from another file:
```python
import xml.etree.ElementTree as etree

with open("table-input.htm", "r") as f:
    read_data = f.read()
    print ("File content:")
    print(read_data)

tree = etree.fromstring(read_data)

with open("table-input.csv", "w") as f:
    for amt, unit, item in tree.getiterator('tr'):
        print("%s,%s,%s" % (amt.text, unit.text, item.text))
        f.write("%s,%s,%s\n" % (amt.text, unit.text, item.text))
```

Reading the HTML code from another file with other libraries and without knowing the dimensions of the table.
See here:
1) https://www.crummy.com/software/BeautifulSoup/bs4/doc/
2) http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

First install pandas and Beautiful Soup:
```bash
sudo apt-get install python3-bs4 python3-pandas
```

```python
import sys
import pandas as pd
from bs4 import BeautifulSoup

def printTableContent(table_to_print):
    row_marker = 0
    for row in table_to_print.find_all('tr'):

        sys.stdout.write(str(row_marker) + " - ")   # sys.stdout.write to avoid new line after the write

        column_marker = 0
        columns = row.find_all('td')
        if (not columns):
            columns = row.find_all('th')

        for column in columns:
            sys.stdout.write(str(column_marker) + "[" + column.get_text() + "]" + "  \t")
            column_marker += 1
     
        row_marker+=1   
        print()
    
def writeTableToFile(table_to_write, filename, separator):
    with open(filename, "w") as f:
        for row in table_to_write.find_all('tr'):
            columns = row.find_all('td')
            if (not columns):
                columns = row.find_all('th')
            for column in columns:
                f.write(column.get_text() + separator)
            f.write("\n")

with open("table-input2.htm", "r") as f:
    read_data = f.read()
    print("File content:")
    print(read_data)

soup = BeautifulSoup(read_data, 'lxml') # Parse the HTML as a string
table1 = soup.find_all('table')[0]      # Grab the first table
table2 = soup.find_all('table')[1]      # Grab the second table

print("This is the first table: \n" + str(table1))
print()
print("This is the second table: \n" + str(table2))
print()

print("Content first table:")
printTableContent(table1)
print()
print("Content second table:")
printTableContent(table2)

print()
print("Writing first table to file table1ToFile.csv, comma separated values")
writeTableToFile(table1,"table1ToFile.csv",",")
print("Writing first table to file table2ToFile.csv, tab separated values")
writeTableToFile(table2,"table2ToFile.csv","\t")
```

## Exercise 12
Extract uppercase words from a file, extract unique words.

See here:
1) https://stackoverflow.com/questions/21107505/python-word-count-from-a-txt-file-program)
2) https://docs.python.org/3/library/collections.html#collections.Counter
3) https://docs.python.org/3/library/stdtypes.html#str.isupper

Opening, printing content and searching for a word in a file, example 1:
```python
def searchWordInFile(word, filename):
    print("-------------------------------------")    
    f = open(filename)
    print("Searching for the word '"+word+"'...")
    c = 0
    lineCount = 0
    lines = []
    for line in f:
        if word in line: 
            c+=1
            lines.append(lineCount)
        lineCount+=1    
    print("Word '"+word+"' found " + str(c) + " times at these lines: " + str(lines))
    print("-------------------------------------")

def openAndPrintFile(filename):
    f = open(filename)  # read mode "r" is set up by default
    print ("Name of the file: ", f.name)
    print("-------------------------------------")
    c=0
    for line in f:
        print(str(c) + " - " + line, end='')
        c+=1
    print("-------------------------------------")
    f.close()

openAndPrintFile("fileToAnalyze.txt")
searchWordInFile("and", "fileToAnalyze.txt")
```

Opening, printing content and searching for a word in a file, example 2:
```python
import collections

def openAndPrintFile(filename):
    f = open(filename)  # read mode "r" is set up by default
    print ("Name of the file: ", f.name)
    print("-------------------------------------")
    c=0
    for line in f:
        print(str(c) + " - " + line, end='')
        c+=1
    print("-------------------------------------")
    f.close()

def listWordsInFile(filename):
    fileToRead = open(filename)
    words = fileToRead.read().split()
    fileToRead.close()
    return words

def countWordInList(listOfWords, wordToSearch):
    c = collections.Counter(listOfWords)
    print("The word '", wordToSearch, "' has been found ", c[wordToSearch], " times.")

openAndPrintFile("fileToAnalyze.txt")
words = listWordsInFile("fileToAnalyze.txt")

print(words)
print("-------------------------------------")
countWordInList(words,"and")
countWordInList(words,"Terre")
countWordInList(words,"PUTIN")
```

Opening, printing content of a file, words frequencies, unique and uppercase words:
```python
def openAndPrintFile(filename):
    f = open(filename)  # read mode "r" is set up by default
    print ("Name of the file: ", f.name)
    print("-------------------------------------")
    c=0
    for line in f:
        print(str(c) + " - " + line, end='')
        c+=1
    print("-------------------------------------")
    f.close()

openAndPrintFile("fileToAnalyze.txt")

file = open("fileToAnalyze.txt", "r", encoding="utf-8-sig")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
file.close()

uniqueWords = []
uppercaseWords = []
for k,v in wordcount.items():
    if k.isupper():
        uppercaseWords.append(k)
    if v==1: 
        print("{0:15} ==> {1}".format(k,v))
        uniqueWords.append(k)
    else:
        print("{0:20} ==> {1}".format(k,v))

print("-------------------------------------")
print("Unique words: ", uniqueWords)
print("-------------------------------------")
print("Uppercase words: ", uppercaseWords)
```

## Exercise 13
Implement word wrapping feature (observe how word wrap works in windows 'notepad').

See here:
1) https://en.wikipedia.org/wiki/Line_wrap_and_word_wrap
2) https://docs.python.org/3.1/library/textwrap.html
3) https://pymotw.com/2/textwrap/

```python
import textwrap

def openAndPrintFile(filename):
    f = open(filename)  # read mode "r" is set up by default
    print ("Name of the file: ", f.name)
    print("-------------------------------------")
    c = 0
    for line in f:
        print(str(c) + " - " + line, end='')
        c += 1
    print("-------------------------------------")
    f.close()

def readFileInAString(fileName):
    with open(fileName) as f3:
        return f3.read()

openAndPrintFile("fileToWordWrap.txt")

lineWidth = int(input("Input line width: "))

wrapped_text = textwrap.wrap(readFileInAString("fileToWordWrap.txt"), lineWidth)
print("\nText wrapped:\n")
print(wrapped_text)
print()
for line in wrapped_text:
    print(line)
```

## Exercise 14
Adding / removing items in the beginning, middle and end of the array.

See [here](https://docs.python.org/3/tutorial/datastructures.html):

```python
numberList = [11,335,749,54,263,678,980,492,10]

print("{0:35} {1:40}".format("Initial list:",str(numberList)))

numberList.insert(0, 0)
print("{0:35} {1:40}".format("Inserted 0 at the beginning:",str(numberList)))

numberList.insert(6, 44)
print("{0:35} {1:40}".format("Inserted 44 at position 6 (from 0):",str(numberList)))

numberList.append(999)
print("{0:35} {1:40}".format("Appended 999 at the end:",str(numberList)))
```

## Exercise 15
Are these features supported by your language: operator overloading, virtual functions, references, pointers, etc.?
Is there something called "namespace / package / module" supported by your language? (Name mangling) - Read More on this.

**15.1) Operator overloading**

From [Wikipedia](https://en.wikipedia.org/wiki/Operator_overloading):

> In programming, **operator overloading**, sometimes termed operator ad hoc polymorphism, is a specific case of polymorphism, where different operators have different implementations depending on their arguments. Operator overloading is generally defined by a programming language, a programmer, or both.

> [...]
> In computer science, **syntactic sugar** is syntax within a programming language that is designed to make things easier to read or to express. Operator overloading is syntactic sugar and is used because it allows programming using notation nearer to the target domain and allows user-defined types a similar level of syntactic support as types built into a language. It is common, for example, in scientific computing, where it allows computing representations of mathematical objects to be manipulated with the same syntax as on paper.  
> [...]
> Operator overloading does not change the expressive power of a language (with functions), as it can be emulated using function calls. For example, consider variables a, b, c of some user-defined type, such as matrices:  
a + b * c  

> In a language that supports operator overloading, and with the usual assumption that the '*' operator has higher precedence than '+' operator, this is a concise way of writing:  
add (a, multiply (b,c))  

> However, the former syntax reflects common mathematical usage.

In Python operators are overloadable by the programmer and they are limited to a predefined set.

Read these:
1) https://docs.python.org/3/reference/datamodel.html#special-method-names
2) http://blog.teamtreehouse.com/operator-overloading-python > https://gist.github.com/kennethlove/56dfeb0d09c52bb4d812
3) https://www.programiz.com/python-programming/operator-overloading
4) http://thepythonguru.com/python-operator-overloading/


**15.2) Virtual functions**

From [Wikipedia](https://en.wikipedia.org/wiki/Virtual_function):

> In object-oriented programming, in languages such as C++, a **virtual function** or **virtual method** is an inheritable and overridable function or method for which dynamic dispatch is facilitated. This concept is an important part of the (runtime) polymorphism portion of object-oriented programming (OOP).

> For example, a base class Animal could have a virtual function _eat_. Subclass Llama would implement eat() differently than subclass Wolf, but one can invoke eat() on any class instance referred to as Animal, and get the eat() behaviour of the specific subclass.

```c++
class Animal {
public:
    void /*non-virtual*/ move(void) { 
        std::cout << "This animal moves in some way" << std::endl; 
    }
    virtual void eat(void) = 0;
};

// The class "Animal" may possess a definition for eat() if desired.
class Llama : public Animal {
public:
    // The non virtual function move() is inherited but not overridden
    void eat(void) override { 
        std::cout << "Llamas eat grass!" << std::endl; 
    }
};
```

Read these:
1) https://stackoverflow.com/questions/4714136/how-to-implement-virtual-methods-in-python
2) http://inspirated.com/2009/05/03/all-methods-in-python-are-effectively-virtual
3) https://docs.python.org/3/library/abc.html
4) http://www.jitendrazaa.com/blog/java/virtual-function-in-java/
5) https://bytes.com/topic/python/answers/23259-can-i-implement-virtual-functions-python

> Virtual functions (using C++ terminology) are something limited to
statically-typed languages. A virtual function call will be resolved
dynamically, based on the runtime type of the object. A non-virtual
call will be resolved at compile-time, based on the declared type of
the object. Since Python is dynamically typed, the only possibility
is for all methods to be "virtual".

**15.3) References and Pointers**

From Wikipedia (https://en.wikipedia.org/wiki/Reference_type):
> In programming language theory, a reference type is a data type that refers to an object in memory. A pointer type on the other hand refers to a memory address. Reference types can be thought of as pointers that are implicitly dereferenced. The objects being referred to are dynamically allocated on the heap whereas value types are allocated automatically on the stack. In languages supporting garbage collection the objects being referred to are destroyed automatically after they become unreachable.
> In Python, classes—including immutable booleans, immutable integer numbers, immutable floating-point numbers, immutable complex numbers, immutable strings, byte strings, immutable byte strings, immutable tuples, immutable ranges, immutable memory views, lists, dictionaries, sets, immutable sets—are reference types.

and also (https://en.wikipedia.org/wiki/Pointer_(computer_programming)):
> In computer science, a pointer is a programming language object, whose value refers to (or "points to") another value stored elsewhere in the computer memory using its memory address. A pointer references a location in memory, and obtaining the value stored at that location is known as dereferencing the pointer.

It can be confusing but to get an easy example see here:  
![alt text](http://assets.iosappsdev.org/objective-c/tutorials/objective-c/media/c-basics/pointers.png "Pointer vs References")

Read these:

1) https://rosettacode.org/wiki/Pointers_and_references#Python
> Python does not have pointers and all Python names (variables) are implicitly references to objects. Python is a late-binding dynamic language in which "variables" are untyped bindings to objects.

1) https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
2) https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/
3) http://stupidpythonideas.blogspot.com.au/2013/11/does-python-pass-by-value-or-by.html
4) http://interactivepython.org/runestone/static/thinkcspy/Lists/ObjectsandReferences.html
5) http://scottlobdell.me/2013/08/understanding-python-variables-as-pointers/
6) https://hbfs.wordpress.com/2011/06/14/python-references-vs-c-and-c/
7) http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#other-languages-have-variables

**15.4) namespace / package / module** 

From [Wikipedia](https://en.wikipedia.org/wiki/Namespace):
> In computing, a namespace is a set of symbols that are used to organize objects of various kinds, so that these objects may be referred to by name. Prominent examples include:
- file systems are namespaces that assign names to files;
- some programming languages organize their variables and subroutines in namespaces;
- computer networks and distributed systems assign names to resources, such as computers, printers, websites, (remote) files, etc.

> For many programming languages, namespace is a context for their identifiers. In an operating system, an example of namespace is a directory. Each name in a directory uniquely identifies one file or subdirectory, but one file may have the same name multiple times.

> As a rule, names in a namespace cannot have more than one meaning; that is, different meanings cannot share the same name in the same namespace. A namespace is also called a context, because the same name in different namespaces can have different meanings, each one appropriate for its namespace.

> Following are other characteristics of namespaces:
- Names in the namespace can represent objects as well as concepts, be the namespace a natural or ethnic language, a constructed language, the technical terminology of a profession, a dialect, a sociolect, or an artificial language (e.g., a programming language).
- In the Java programming language, identifiers that appear in namespaces have a short (local) name and a unique long "qualified" name for use outside the namespace.
- Some compilers (for languages such as C++) combine namespaces and names for internal use in the compiler in a process called name mangling.

> In some programming languages (e.g. C++, Python), the identifiers naming namespaces are themselves associated with an enclosing namespace. Thus, in these languages namespaces can nest, forming a namespace tree. At the root of this tree is the unnamed global namespace.

> In Python, namespaces are defined by the individual modules, and since modules can be contained in hierarchical packages, then name spaces are hierarchical too. In general when a module is imported then the names defined in the module are defined via that module's name space, and are accessed in from the calling modules by using the fully qualified name.

```python
# assume modulea defines two functions : func1() and func2() and one class : class1
import modulea

modulea.func1()
modulea.func2()
a = modulea.class1()
```

> The "from ... import ..." can be used to insert the relevant names directly into the calling module's namespace, and those names can be accessed from the calling module without the qualified name:

```python
# assume modulea defines two functions : func1() and func2() and one class : class1
from modulea import func1

func1()
func2() # this will fail as an undefined name, as will the full name modulea.func2()
a = class1() # this will fail as an undefined name, as will the full name modulea.class1()
```

> Since this directly imports names (without qualification) it can overwrite existing names with no warnings.

> A special form is "from ... import *", which imports all names defined in the named package directly in the calling modules namespace. Use of this form of import, although supported within the language, is generally discouraged as it pollutes the namespace of the calling module and will cause already defined names to be overwritten in the case of name clashes.
Python also supports "import x as y" as a way of providing an alias or alternative name for use by the calling module:

```python
import numpy as np
a = np.arange(1000)
```

Read these:

1) https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
2) https://www.programiz.com/python-programming/namespace 
3) https://docs.python.org/3/tutorial/modules.html
4) https://docs.python.org/3/tutorial/modules.html#packages
5) https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package

**15.5) name mangling**

From [Wikipedia](https://en.wikipedia.org/wiki/Name_mangling):
> In compiler construction, name mangling (also called name decoration) is a technique used to solve various problems caused by the need to resolve unique names for programming entities in many modern programming languages.
It provides a way of encoding additional information in the name of a function, structure, class or another datatype in order to pass more semantic information from the compilers to linkers.
The need arises where the language allows different entities to be named with the same identifier as long as they occupy a different namespace (where a namespace is typically defined by a module, class, or explicit namespace directive) or have different signatures (such as function overloading).
Any object code produced by compilers is usually linked with other pieces of object code (produced by the same or another compiler) by a type of program called a linker. The linker needs a great deal of information on each program entity. For example, to correctly link a function it needs its name, the number of arguments and their types, and so on.

> In Python, mangling is used for "private" class members which are designated as such by giving them a name with two leading underscores and no more than one trailing underscore. For example, \_\_thing will be mangled, as will \_\_\_thing and \_\_thing\_, but \_\_thing\_\_ and \_\_thing\_\_\_ will not. Python's runtime does not restrict access to such members, the mangling only prevents name collisions if a derived class defines a member with the same name.

On encountering name mangled attributes, Python transforms these names by a single underscore and the name of the enclosing class, for example:

```python
>>> class Test(object):
...     def __mangled_name(self):
...         pass
...     def normal_name(self):
...         pass
>>> t = Test()
>>> [attr for attr in dir(t) if 'name' in attr]
['_Test__mangled_name', 'normal_name']
```

Read these:
1) https://docs.python.org/3/tutorial/classes.html#private-variables
2) https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
