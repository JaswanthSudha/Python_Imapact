class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
    	return f"{self.data}"
n=int(input("enter number of Nodes"))-1
value=int(input("enter the root"))
root=Node(value)
while n!=0:
    left=int(input("enter leftNode of {root.data}"))
    right=int(input("enter rightNode of {root.data}"))
    if left is not None:
        root.left=Node(left)
        n-=1
    if right is not None:
        root.right=Node(right)
        n-=1
    
    

