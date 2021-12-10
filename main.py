a=int(input("enter a no1: "))
b=int(input("enter a no2: "))
if a<b:
    n=a
else:
    n=b
for i in range(1,n+1):
    if (a%i==0 and b%i==0):
        gcd=i
print(gcd)