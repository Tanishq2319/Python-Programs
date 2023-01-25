x=int(input("enter a number"))
z=x
rev=0
while(x>0):
    rem=x%10
    rev=rev*10+rem
    x=x//10
if(z==rev):
    print("palindrome")
else:
    print("not palindrome")