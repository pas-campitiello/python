# It sorts the list of pairs using as key the second value of each pair.

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# It creates a list of squares until 10
print(list(map(lambda x: x**2, range(10))))
