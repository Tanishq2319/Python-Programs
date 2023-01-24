s1=input()
s2=input()
s=s1+s2
leng=len(s)
k=""
z=""
for i in range(0,leng):
    if(s[i]=="A"):
        z=s[i].lower()
        k=k+z
    else:
        k=k+s[i]
print (k)