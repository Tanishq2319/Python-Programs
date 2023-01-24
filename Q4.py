import string
str1=""
c1=input()
c2=input()
for i in string.ascii_lowercase:
    str1=str1+i
dist=str1.rfind(c1)-str1.find(c2)
print(dist*-1)