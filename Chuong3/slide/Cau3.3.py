a=int(input("Tieu thu="))
gia1=550
gia2=750
gia3=950
gia4=1350
if a<=100:
    b=a*gia1
elif a<=150:
    b=100*gia1+(a-100)*gia2
elif a<=200:
    b=100*gia1+(a-150)*gia3+50*gia2
else:
    b=100*gia1+(a-200)*gia4+50*gia2+50*gia3
c=b*1.1
print("Phai tra=",c,sep="")