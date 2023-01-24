import math
numbers=[]
square_roots=[]
s=int(input("Enter the no of elements: "))
print ("Enter the values for list")
for i in range(s):
    val=int(input())
    numbers.append(val)
print("your list")
print(numbers)
for num in numbers:
    root=math.sqrt(num)
    square_roots.append(root)
print ("Square roots")
print(square_roots)