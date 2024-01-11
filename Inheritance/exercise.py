from math import pow,pi
class Circle:
    radius=0
    def __init__(self):
        pass
    def area(self,radius):
        self.radius=radius
        return  pi*pow(self.radius,2)
class Cylinder(Circle):
    radius=0
    def __init__(self,height):
        self.height=height
    def area(self,radius):
        self.radius=radius
        value=super().area(self.radius)
        return 2*value+(2*pi*self.radius*self.height)
    def volume(self):
        return f"volume of Cylinder {pi*pow(2,self.radius)*self.height}"
circle=Circle()
print(circle.area(10))
cylinder=Cylinder(height=10)
print(cylinder.area(10))
print(cylinder.volume())