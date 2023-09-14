def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def sub(a,b):
    return a-b
while True:
    n1=int(input("what's the first numbar?: \n"))
    print(""" 
    +
    -
    *
    /
    """)
    while True:
        operation=input("pick a operation \n")
        n2=int(input("what's the next number \n"))
        if operation=="+":
            result=add(n1,n2)
        elif operation=="-":
            result=sub(n1,n2)
        elif operation=="*":
            result=multiply(n1,n2)
        elif operation=="/":
            result=divide(n1,n2)
        else:
            print("wrong Input")
        print(n1 , operation , n2, "=",result)
        res=input(f"Type 'y' to continue with {result} . else type 'n' to start a new calculation. else type 'exit' \n").lower()
        if res=='y':
            n1=result
        elif res=='n':
            break
        else:
            break
        
            
            
    