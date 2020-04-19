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
