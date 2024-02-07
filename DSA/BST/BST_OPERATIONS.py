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
	return "node inserted Successfully"
def insert(rootNode,nodeValue):
	if rootNode is None:
		rootNode.data=nodeValue
	else:
		pass
rootNode=BSTNode(None)
insertNode(rootNode,70)
insertNode(rootNode,90)
insertNode(rootNode,60)
insertNode(rootNode,45)
insertNode(rootNode,100)
insertNode(rootNode,50)
insertNode(rootNode,80)
