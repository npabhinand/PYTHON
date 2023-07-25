#inheritance

class Mammal:
    def walk(self):
        print("mammals can walk")
        
        
class Cat(Mammal):
    pass
class Dog(Mammal):
    def bark(self):
        print("dogs can bark")
dog=Dog()
dog.walk()
dog.bark()      

        