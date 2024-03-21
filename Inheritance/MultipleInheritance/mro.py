class A:
    def m1(self):
        return "a of m"
class B(A):
    pass
class C(A):
    pass
class D(C,B):
    pass
obj=D()
print(obj.m1())