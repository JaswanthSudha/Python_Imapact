from tree import t1,n1
def identical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None and root2 is not None:
        return False
    if root1 is not None and root2 is None:
        return False
    if root1.data==root2.data:
        left=identical(root1.left,root2.left)
        right=identical(root1.right,root2.right)
        if left and right:
            return True
        else:
            return False
    return False

ans=identical(t1,n1)
print(ans)
