nums = []
sum=0
s=int(input("enter the number of elements"))
for i in range(s):
    val=int(input())
    nums.append(val)
for i in range(s):
    if (nums[i]%2==0):
        sum = sum + nums[i]
print("\nSum of Even Numbers is", sum)
