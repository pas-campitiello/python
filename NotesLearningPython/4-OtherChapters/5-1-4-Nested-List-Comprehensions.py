matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = []

print([row[3] for row in matrix])

for i in range(4):
    transposed.append([row[i] for row in matrix])

print("Matrix:     ", matrix)
print("Transposed: ", transposed)

print("----------------------")

transposedAgain = []
for i in range(3):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in transposed:
        transposed_row.append(row[i])
    transposedAgain.append(transposed_row)

print("Transposed again: ", transposedAgain)

print("----------------------")
print("Transposed using zip(): ", list(zip(*matrix)))
