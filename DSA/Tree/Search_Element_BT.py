# import Queue
from Queue import queue
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def search(root,value):
    if root ==None:
        return "NO Binary Tree"
    else:
        custom=queue()
        custom.enqueue(root)
        while not custom.isEmpty():
            node=custom.dequeue()
            if node.data==value.data:
                return "Found"
            if node.left is not None:
                custom.enqueue(node.left)
            if node.right is not None:
                custom.enqueue(node.right)
        return "Not Found"
root=Node(1)
node1=Node(2)
node2=Node(3)
root.left=node1
root.right=node2
left_1=Node(4)
right_1=Node(5)
node1.left=left_1
node1.right=right_1
print(search(root,Node(4)))


