from Tree_Create import root
from Queue import queue
from Tree_Create import Node
from LevelOrder import LevelOrder
def delete_deep_node(rootNode):
	if rootNode==None:
		return "No Binary Tree"
	else:
		custom_queue=queue()
		custom_queue.enqueue(rootNode)
		while not custom_queue.isEmpty():
			node=custom_queue.dequeue()
			if node.left is not None:
				custom_queue.enqueue(node.left)
			if node.right is not None:
				custom_queue.enqueue(node.right)
		ans=Node(node.data)
		node.data=None
		return ans
def delete_node(rootNode,nodeDelete):
	if rootNode is None:
		return "BT Not Exist"
	else:
		custom_queue=queue()
		custom_queue.enqueue(rootNode)
		while not custom_queue.isEmpty():
			node=custom_queue.dequeue()
			if node.data==nodeDelete.data:
				deepest_node=delete_deep_node(rootNode)
				node.data=deepest_node.data
				return "Deleted"
			else:
				if node.left is not None:
					custom_queue.enqueue(node.left)
				if node.right is not None:
					custom_queue.enqueue(node.right)
		return "Unable to Delete"
def delete_tree(rootNode):
	if rootNode==None:
		return 
	rootNode.data=None
	rootNode.left=None
	rootNode.right=None
# print(delete_node(root,Node(3)))
print("Before deleting Tree")
print("")
LevelOrder(root)
delete_tree(root)
print("After deleting Tree")
LevelOrder(root)


