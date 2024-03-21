class Node:
    def __init__(self,data):
        self.data=data
        self.ptr=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.ptr=n2
n2.ptr=n3
head=n1
while head:
    print(head.data,end="->")
    head=head.ptr
    if head ==None:
        print("None")

