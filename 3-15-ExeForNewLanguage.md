
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
        if c == 27:
            break   # Exit the while loop for ES

curses.wrapper(main)
```

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
