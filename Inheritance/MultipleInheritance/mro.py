class A:
    def m(self):
        print("m of A called")
class B:
    def m(self):
        print("m of B called")
class C(A,B):
    pass
print(C.__mro__)