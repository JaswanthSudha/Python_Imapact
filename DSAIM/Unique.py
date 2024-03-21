class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def bstTree(root,data):
    if root is None:
        root=Node(data)
    elif root.data>data:
        if root.left is None:
            root.left=Node(data)
        else:
            bstTree(root.left,data)
    else:
        if root.right is None:
            root.right=Node(data)
        else:
            bstTree(root.right,data)
def preOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
root=Node(1)
for i in range(2,4):
    bstTree(root,i)
preOrder(root)


    