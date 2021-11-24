l=[]
n=int(input("enter total numbers of elements"))
for i in range(0,n):
    a=int(input("enter the elements"))
    l.append(a)
print(l)
print("after deleting numbers")
for i in l:
     if(i%2==0):
       l.remove(i)
print(l)
          



