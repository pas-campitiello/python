numberList = [11,335,749,54,263,678,980,492,10]

print("{0:35} {1:40}".format("Initial list:",str(numberList)))

numberList.insert(0, 0)
print("{0:35} {1:40}".format("Inserted 0 at the beginning:",str(numberList)))

numberList.insert(6, 44)
print("{0:35} {1:40}".format("Inserted 44 at position 6 (from 0):",str(numberList)))

numberList.append(999)
print("{0:35} {1:40}".format("Appended 999 at the end:",str(numberList)))
