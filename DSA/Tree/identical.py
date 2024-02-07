class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def postOrder(root):
    if root is None:
        return 
    postOrder(root.left)
    print(root.data)
    postOrder(root.right)
def identical(root1,root2):
    if root1 is None and root2 is None:
        return 1
    if root1.data ==root2.data:
        identical(root1.left,root2.left)
        identical(root1.right,root2.right)
        return 1
    else:
        return 0
n1=Node(1)
t1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
t2=Node(2)
t3=Node(3)
t4=Node(4)
t5=Node(6)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
t1.left=t2
t1.right=t3
t2.left=t4
t2.right=t5
print(identical(n1,t1))
