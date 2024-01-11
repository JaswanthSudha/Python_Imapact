class Parent:
    def __init__(self):
        print("Parent Class")
class Child(Parent):
    def __init__(self):
        super().__init__()
class Rectangle:
    def __init__(self):
        self.h=10
        self.b=10
    def method(self):
        print('Parent class')
class Cuboid(Rectangle):
    def __init__(self):
        # Rectangle.__init__(self)#super keyword
        super().__init__();#we should not pass self keyword python will automatically pass the self keyword
        self.v=10
    def volume(self):
        return self.h*self.b*self.v
    def method(self):
        super().method()
        print("child class")
class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return f"The age is {self.age} and Name is {self.name}"
class Emp(Person):
    def __init__(self,age,name,sal):
        super().__init__(age,name)
        self.sal=sal
    
    # def __str__(self):
    #     return f"salary is {self.sal}"
        
# cube=Cuboid()
# print(cube.volume())
# cube.method()
empolyee=Emp(10,"Jashu",1000)
print(empolyee)