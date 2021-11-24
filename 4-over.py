n=input("enter the numbers ")
a=n.split(' ')
b=list(map(int,a))
print(n)
le=len(a)
for i in range(le):
    if b[i]>=100:
        a="over"
        b[i]='over'
print(b)
    
