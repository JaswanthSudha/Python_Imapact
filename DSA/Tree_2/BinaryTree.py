class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
	def __str__(self):
		return f"{self.data}"
root=Node(10)
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)
root.left=node1
root.right=node2
node2.left=node3
node2.right=node4
node4.left=node5
node4.right=node6
