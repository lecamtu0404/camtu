x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
if ch=="+":
    c=x+y
elif ch=="-": c=x-y
elif ch=="*": c=x*y
elif ch=="/": c=x/y
else: print("Khong hop le")
print(str(x)+str(ch)+str(y)+"="+str(round(c,1)))