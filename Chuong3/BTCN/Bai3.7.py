def tinhgiaithua(n):
    giaithua =1;
    if (n==0):
        tinhgiaithua(n)==1
    for i in range(1,n+1):
        giaithua=giaithua*i;
        tinhgiaithua(n)==giaithua*i
n=int(input())
print(tinhgiaithua(n))