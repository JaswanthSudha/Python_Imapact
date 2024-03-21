
from Graph.Queue import queue
def LevelOrder(rootNode):
	if rootNode is None:
		return
	else:
		custom_queue=queue()
		custom_queue.enqueue(rootNode)
		while not custom_queue.isEmpty():
			node=custom_queue.dequeue()
			if node.data is not None:
				print(node.data,end=",")
			if node.left is not None:
				custom_queue.enqueue(node.left)
			if node.right is not None:
				custom_queue.enqueue(node.right)
		print("End",end="")
def inorder(rootNode):
	if rootNode is None:
		return
	inOrder(rootNode.left)
	print(rootNode.data)
	inOrder(rootNode.right)
def remove_duplicated(array):
	new_set=set(array)
	return list(new_set)
class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
class BST_CREATE:
	def insert(self,rootNode,nodeData):
		if rootNode==None:
			rootNode.data=nodeData
		if rootNode.data>nodeData:
			if rootNode.left is None:
				node=Node(nodeData)
				rootNode.left=node
			else:
				self.insert(rootNode.left,nodeData)
		else:
			if rootNode.right is None:
				node=Node(nodeData)
				rootNode.right=node
			else:
				self.insert(rootNode.right,nodeData)

inOrder    = [4, 8, 10, 12, 14, 20, 22]
levelOrder = [20, 8, 22, 4, 12, 10, 14]
root_element=levelOrder[0]
root_Node=Node(root_element)
final_list=[]
final_list.extend(inOrder)
final_list.extend(levelOrder)
final_list=remove_duplicated(final_list)
bst=BST_CREATE()
for item in final_list:
	bst.insert(root_Node,item)
LevelOrder(root_Node)



