from Queue import queue
def levelOrder(rootNode):
	if root is None:
		return "No Tree"
	else:
		custom_queue=queue()
		custom_queue.enqueue(rootNode)
		while not custom_queue.isEmpty():
			node=custom_queue.dequeue()
			if node.data is not None:
				print(node.data,end=" ")
			if node.left is not None:
				custom_queue.push(node.right)
			if node.right is not None:
				custom_queue.enqueue(node.right)
		print("End")