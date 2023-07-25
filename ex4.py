#exception handling
try:
    age=int(input("age: "))
    print(age)
    risk=20000/age
    print(risk)
except ZeroDivisionError:
    print("Type age greater than 0")
except ValueError:
    print("invalid input")