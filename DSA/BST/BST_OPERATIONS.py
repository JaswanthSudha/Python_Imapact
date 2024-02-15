class BSTNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
def insertNode(rootNode,nodeValue):
	if rootNode.data is None:
		rootNode.data=nodeValue
	elif rootNode.data>nodeValue:
		if rootNode.left is None:
			rootNode.left=BSTNode(nodeValue)
		else:
			insertNode(rootNode.left,nodeValue)
	else:
		if rootNode.right is None:
			rootNode.right=BSTNode(nodeValue)
		else:
			insertNode(rootNode.right,nodeValue)
def fullBinary(rootNode):
	if rootNode.left is None and rootNode.right is None:
		return True
	if rootNode.left is not None and rootNode.right is None:
		return False
	if rootNode.left is None and rootNode.right is not None:
		return False
	left=fullBinary(rootNode.left)
	right=fullBinary(rootNode.right)
	if left==True and right==True:
		return True
	else:
		return False
test=int(input())
for _ in range(test):
	rootNode=BSTNode(None)
	array=list(map(int,input().split()))
	for i in range(len(array)):
		insertNode(rootNode,array[i])
	ans=fullBinary(rootNode)
	if ans==True:
		print("Yes")
	else:
		print("No")
	print("")
