list=[]
s=int(input("enter the number of elements"))
print ("Enter the values for list")
for i in range(s):
    val=int(input())
    list.append(val)
odd=[num for num in list if num % 2 != 0]
print("Odd numbers:", odd)