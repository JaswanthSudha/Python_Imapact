class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getname(self):
        return self.name
    def getage(self):
        return self.age
class Student:
    def __init__(self,roll,per):
        self.roll=roll
        self.per=per
    def getroll(self):
        return self.roll
    def getper(self):
        return self.per
class ScienceStudent(Person,Student):
    def __init__(self, name, age,roll,per):
        super().__init__(name, age)
        Student.__init__(self,roll,per)
obj=ScienceStudent("jashu",10,62,2)
print(obj.getname())
print(obj.getage())
print(obj.getper())
print(obj.getroll())