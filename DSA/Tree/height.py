class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
def height(root):
	if root==None:
		return 0
	left=height(root.left)
	right=height(root.right)
	if left>right:
		return left+1
	else:
		return right+1
root=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
root.left=node2
root.right=node3
node2.left=node4
node2.right=node5
print(height(root))