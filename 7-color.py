a=input("enter the colrs in set1=") 
b=input("enter the colors in set2=")
a=a.split(',')
b=b.split(',')
a=set(a)
b=set(b)
print(a)
print(b)
print(a.difference(b))

