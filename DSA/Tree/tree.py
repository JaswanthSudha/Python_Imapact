class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def postOrder(root):
     if root is None:
        return 
     postOrder(root.left)
     print(root.data,end=" ")
     postOrder(root.right)        
n1=Node(1)
t1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
t2=Node(2)
t3=Node(3)
t4=Node(4)
t5=Node(5)
# n1.left=n2
# n1.right=n3
# n2.left=n4
# n2.right=n5
# t1.left=t2
# t1.right=t3
# t2.left=t4
# t2.right=t5
# postOrder(t1)
newRoot=Node(1)
newRoot.left=n2
newRoot.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
# postOrder(newRoot)

