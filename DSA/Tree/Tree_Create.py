class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
    	return f"{self.data}"
root=Node(1)
node1=Node(2)
node2=Node(3)
root.left=node1
root.right=node2
left_1=Node(4)
right_1=Node(5)
node1.left=left_1
node1.right=right_1