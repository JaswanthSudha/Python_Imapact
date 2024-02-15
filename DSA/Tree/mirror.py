from tree import newRoot
class newNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def mirror(root):
    if root is None:
        return None
    else:
        left_mirror=mirror(root.left)
        right_mirror=mirror(root.right)
        root.right,root.left=left_mirror,right_mirror
        return root
def inOrder(root):
    if root is None:
        return 
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)
final_root= mirror(newRoot)
inOrder(final_root)
