a=int(input("yrsOfService= "))
b=int(input("salary= "))
bonus=0
if a < 5:
    if b < 500:
        bonus = 100
    else:
        bonus = 200
else:
    bonus = 700
print("Bonus amount: ", bonus)