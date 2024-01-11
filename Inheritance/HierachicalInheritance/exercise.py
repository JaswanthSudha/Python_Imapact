class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self) -> str:
        return f"{self.name},{self.age}"
class Teacher(SchoolMember):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary=salary
    def __str__(self) -> str:
        value=super().__str__()
        return f"{value},{self.salary}"
class Student(SchoolMember):
    def __init__(self, name, age,fees):
        super().__init__(name, age)
        self.fees=fees
    def __str__(self) -> str:
        value= super().__str__()
        return f"{value},{self.fees}"
teacher=Teacher("JayPrakash",10,10000)
student=Student("Jaswanth",23,10000000)
print(teacher)
print(student)
