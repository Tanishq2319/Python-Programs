#square of all numbers except factors of 3
print("Enter the range")
n1=int(input("starting point:-"))
n2=int(input("ending point:-"))
for i in range(n1,n2):
    if(i%3!=0):
        print(i*i)
    else:
        continue