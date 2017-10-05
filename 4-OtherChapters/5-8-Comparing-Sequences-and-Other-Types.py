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
