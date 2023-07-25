## class
# class Point:
#     def __init__(self , x, y):
#         self.x=x
#         self.y=y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# point=Point(10,20)
# point.move()
# point.y=30
# print(point.x,point.y)

class Person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f"{self.name} can talk")
        
person=Person('abhinand')
person.talk()
print(person.name)

        
