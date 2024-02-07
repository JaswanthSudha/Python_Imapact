from BinaryTree import root
def depth(root):
	if root==None:
		return -1
	left=depth(root.left)
	right=depth(root.right)
	if left>right:
		return left+1
	else:
		return right+1
print(depth(root))
