# Other important things from the official tutorial
Official tutorial: https://docs.python.org/3/tutorial/index.html


## 4.7.5 Lambda expressions
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Probably the most useful way to exploit lambda functions is define them in-line and/or in small function as an argument:

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
```

**list.sort()**  
https://docs.python.org/3/library/stdtypes.html#list.sort

Key specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used for the entire sorting process. The default value of None means that list items are sorted directly without calculating a separate key value.

**map()**  
https://docs.python.org/3/library/functions.html#map



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

```

## 5.2 The del statement
https://docs.python.org/3/tutorial/datastructures.html#the-del-statement

``` python

```


## 5.3 Tuples and Sequences
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

``` python

```


## 5.4 Sets
https://docs.python.org/3/tutorial/datastructures.html#sets

``` python

```


## 5.5 Dictionaries
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

``` python

```


## 5.6 Looping techniques
https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

``` python

```


## 5.7 More on conditions
https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions

``` python

```


## 5.8. Comparing Sequences and Other Types
https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types

``` python

```


## 6.3. The dir() Function
https://docs.python.org/3/tutorial/modules.html#the-dir-function

```python
```

## 7.1 Fancier Output Formatting
https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting

```python
```

## 7.2.2. Saving structured data with json
https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json

```python
```


## 9.3 A first look at classes
https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes

```python
```

## 9.4 Random remarks
https://docs.python.org/3/tutorial/classes.html#random-remarks


## 9.5 Inheritance
https://docs.python.org/3/tutorial/classes.html#inheritance

## 9.6 Private variables
https://docs.python.org/3/tutorial/classes.html#private-variables

## 9.7 Odds and Ends
https://docs.python.org/3/tutorial/classes.html#odds-and-ends

## 9.8-9-10 Iterators and Generators
https://docs.python.org/3/tutorial/classes.html#iterators
https://docs.python.org/3/tutorial/classes.html#generators
https://docs.python.org/3/tutorial/classes.html#generator-expressions


## 10. Brief Tour of the Standard Library
https://docs.python.org/3/tutorial/stdlib.html

```python
```

## 11. Brief Tour of the Standard Library II
https://docs.python.org/3/tutorial/stdlib2.html

```python
```

## 12. Virtual Environments and Packages
https://docs.python.org/3/tutorial/venv.html

```python
```

## 99. Other points
https://www.stavros.io/tutorials/python/

```python
```
