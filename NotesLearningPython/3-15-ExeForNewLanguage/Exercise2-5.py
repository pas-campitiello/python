num = 0
numlist = []
while True:
    num = input("Insert a number: ")
    if num=="q": break    
    numlist.append(int(num))

print("List: ",numlist)
print("Max: ",max(numlist))
print("Min: ",min(numlist))

