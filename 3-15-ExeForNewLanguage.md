
# 15 exercises for learning Python
Inspired by: http://www.ign.com/boards/threads/15-exercises-for-learning-a-new-programming-language.129542936/


## Exercise 1
Display series of numbers (1,2,3,4, 5....etc) in an infinite loop.  
The program should quit if someone hits a specific key (Say ESCAPE key).

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

Reading [here](http://forums.xkcd.com/viewtopic.php?t=99890) I discovered the thread example; modifying it slightly it looks like:
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
Now this is solutions works pretty well except that it prints the numbers with some initial spaces.


## Exercise 2
Fibonacci series, swapping two variables, finding maximum/minimum among a list of numbers.

## Exercise 3
Accepting series of numbers, strings from keyboard and sorting them ascending, descending order.

## Exercise 4
Reynolds number is calculated using formula (D*v*rho)/mu Where D = Diameter, V= velocity, rho = density mu = viscosity
Write a program that will accept all values in appropriate units (Don't worry about unit conversion)
If number is < 2100, display Laminar flow,
If it’s between 2100 and 4000 display 'Transient flow' and
if more than '4000', display 'Turbulent Flow' (If, else, then...)

## Exercise 5
Modify the above program such that it will ask for 'Do you want to calculate again (y/n),
if you say 'y', it'll again ask the parameters. If 'n', it'll exit. (Do while loop)

While running the program give value mu = 0. See what happens. Does it give 'DIVIDE BY ZERO' error?
Does it give 'Segmentation fault..core dump?'. How to handle this situation. Is there something built
in the language itself? (Exception Handling)

## Exercise 6
Scientific calculator supporting addition, subtraction, multiplication, division, square-root, square, cube,
sin, cos, tan, Factorial, inverse, modulus

## Exercise 7
Printing output in different formats (say rounding up to 5 decimal places, truncating after 4 decimal places,
padding zeros to the right and left, right and left justification)(Input output operations)

## Exercise 8
Open a text file and convert it into HTML file. (File operations/Strings)

## Exercise 9
Time and Date : Get system time and convert it in different formats 'DD-MON-YYYY', 'mm-dd-yyyy', 'dd/mm/yy' etc.

## Exercise 10
Create files with date and time stamp appended to the name

## Exercise 11
Input is HTML table, Remove all tags and put data in a comma/tab separated file.

## Exercise 12
Extract uppercase words from a file, extract unique words

## Exercise 13
Implement word wrapping feature (Observe how word wrap works in windows 'notepad')

## Exercise 14
Adding/removing items in the beginning, middle and end of the array.

## Exercise 15
Are these features supported by your language: Operator overloading, virtual functions, references, pointers etc.
Is there something called 'namespace / package / module' supported by your language? (Name mangling) - Read More on this.
