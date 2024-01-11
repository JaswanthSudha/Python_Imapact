class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
        print("Person constructor called")
    def __str__(self):
        return f"name is {self.name} and age is {self.age}"
class Emp(Person):
    def __init__(self,id,sal,age,name):
        super().__init__(age,name)
        self.id=id
        self.sal=sal
        print("Empolyee constructor called")
    def income(self):
        return f"income {self.sal+self.bonus}"
    def __str__(self):
        return f"name is {self.name} age is {self.age} id is {self.id} sal is {self.sal}"
class Manager(Emp):
    def __init__(self,id,sal,age,name,bonus):
        super().__init__(id,sal,age,name)
        self.bonus=bonus
        print("Manager constructor called")
    def __str__(self):
        return f"name is {self.name} age is {self.age} id is {self.id} sal is {self.sal} bonus{self.bonus}"
manager=Manager(1,10000,24,"jashu",1000)
print(manager)
print(f"Manager's Salary:{manager.sal}")
income=manager.income()
print(f"Manager's Total Income {income}")
