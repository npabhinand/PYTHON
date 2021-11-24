x={}
a=int(input("enter the size of dictionary"))
for i in range(a) :
      key=input("enter key")
      value=input("enter value")
      x[key]=value
print(x)

for i in sorted(x.keys()):
      print(i,x[i])

for i in sorted(x.keys(),reverse=True):
      print(i,x[i])

    
