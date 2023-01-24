n=input()
cl=0
cd=0
for i in n:
    if(i.isalpha()):
        cl+=1
    elif(i.isdigit()):
        cd+=1
print("char",cl)
print("digit",cd)