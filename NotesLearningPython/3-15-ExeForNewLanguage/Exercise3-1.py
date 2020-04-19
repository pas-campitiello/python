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
