from Queue import queue
from Tree_Create import root
def LevelOrder(rootNode):
	if rootNode is None:
		return
	else:
		custom_queue=queue()
		custom_queue.enqueue(rootNode)
		while not custom_queue.isEmpty():
			node=custom_queue.dequeue()
			if node.data is not None:
				print(node,end=",")
			if node.left is not None:
				custom_queue.enqueue(node.left)
			if node.right is not None:
				custom_queue.enqueue(node.right)
		print("End",end="")
# LevelOrder(root)



