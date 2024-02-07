from Tree_Create import root,Node
from LevelOrder import LevelOrder
def height(rootNode):
	if rootNode ==None:
		return -1
	left=height(rootNode.left)
	right=height(rootNode.right)
	if left>=right:
		return left+1
	else:
		return right+1
node=Node(10)
left=Node(20)
right=Node(30)
node.left=left
node.right=right
print(height(node))
