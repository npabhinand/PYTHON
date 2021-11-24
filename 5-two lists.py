a=input("enter integer values")
b=input("enter some integer values")
a=a.split(' ')
c=list(map(int,a))
b=b.split(' ')
d=list(map(int,b))
len_a=len(c)
len_b=len(d)
flag=0
if(len_a==len_b):
        print("lists are of same length")
else:
        print("lists are not same length")
if sum(c)==sum(d):
    print("sums are equal",sum(c))
else:
    print("sum are not equal")
for i in range(len_a):
    for j in range(len_a):
        if c[i]==d[j]:
            print("occurs in both")
            flag+=1
if flag==0:
    print("not occurs in both")
            

