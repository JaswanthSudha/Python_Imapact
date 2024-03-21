class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def insertNode(rootNode,data):
    if rootNode is None:
        rootNode=Node(data)
    elif rootNode.data>data:
        if rootNode.left is None:
            rootNode.left=Node(data)
        else:
            insertNode(rootNode.left,data)
    elif rootNode.data<data:
        if rootNode.right is None:
            rootNode.right=Node(data)
        else:
            insertNode(rootNode.right,data)
def inOrder(root):
    if root is None:
        return 
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)
def postOrder(root):
    if root is None:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
def preOrder(root,data,flag):
    if root is None:
        return
    if data==root.data:
        return
    preOrder(root.left,data,flag)
    preOrder(root.right,data,flag)
array=list(map(int,input().split()))
rootNode=Node(array[0])
for i in range(1,len(array)):
    insertNode(rootNode,array[i])
# ans=preOrder(rootNode,11)
flag=False
preOrder(rootNode,11,flag)
print(flag)




