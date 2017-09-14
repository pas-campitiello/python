
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

```python
```

## Exercise 13
Implement word wrapping feature (Observe how word wrap works in windows 'notepad')

```python
```

## Exercise 14
Adding/removing items in the beginning, middle and end of the array.

```python
```

## Exercise 15
Are these features supported by your language: Operator overloading, virtual functions, references, pointers etc.
Is there something called 'namespace / package / module' supported by your language? (Name mangling) - Read More on this.

```python
```
