a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=0
min=0
if a>b and a>c:
    max=a
if b>a and b>c:
    max=b
if c>a and c>b:
    max=c
if a<b and a<c:
    min=a
if b<a and b<c:
    min=b
if c<a and c<b:
    min=c
print("SLN=",max,sep="")
print("SBN=",min,sep="")