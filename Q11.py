#convert lower to upper and vice versa
s=input()
leng=len(s)
str=""
for i in range(0,leng):
    k=""
    if(s[i].islower()==True):
        k=s[i].upper()
    else:
        k=s[i].lower()
    str=str+k
print(str)