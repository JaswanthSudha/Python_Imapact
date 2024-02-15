class newNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def height(root):
    if root is None:
        return -1
    else:
        left=height(root.left)
        right=height(root.right)
        if left>right:
            return left+1
        else:
            return right+1
def depth(root):
    if root is None:
        return 
    depth(root.left)
    depth(root.right)
    leftHeight=height(root.left)
    rightHeight=height(root.right)
    if max(leftHeight,rightHeight)-max(rightHeight,leftHeight)<=1:
        return True
    else:
        return False
# root=newNode(1)
# root.left=newNode(2)
# root.right=newNode(3)
# root.left.left=newNode(6)
# root.left.right=newNode(7)
# root.right.left=newNode(8)
# root.right.right=newNode(9)
# root.right.right.left=newNode(10)
# root.right.right.right=newNode(11)
    pass
root=newNode(10)
root.left=newNode(11)
root.right=newNode(12)
print(depth(root.left))


# # leftHeight=height(root.left)+1
# # rightHeight=height(root.right)+1
# # minValue=min(leftHeight,rightHeight)
# # maxValue=max(leftHeight,rightHeight)
# # if maxValue-minValue==1:
# #     print("yes")
# # else:
# #     print("no")
# print(height(root))
    
# # postOrder(root)

# def postOrder(root):
#     if root is None:
#         return 
#     postOrder(root.left)
#     print(root.data)
#     postOrder(root.right)