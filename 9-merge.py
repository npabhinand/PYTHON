x={}
y={}
a=int(input("enter the size of dictionary"))
for i in range(a) :
      key=input("enter key")
      value=input("enter value")
      x[key]=value
b=int(input("enter the size of dictionary"))
for i in range(b) :
      key=input("enter key")
      value=input("enter value")
      y[key]=value
x.update(y)
print(x)
