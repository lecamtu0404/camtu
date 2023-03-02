a=int(input("M1="))
b=int(input("M2="))
c=int(input("M3="))
d=int(input("S="))
if d<=100:
    e=d*a
elif d<=150: e=100*a+(d-100)*b
else: e=100*a+50*b+(d-150)*c
print("Phai tra=",e,sep="")