from BST_OPERATIONS import rootNode
def test_function():
	assert search(rootNode,90)=="Found"
def test_function2():
	assert search(rootNode,100)=="Found"
def search(rootNode,nodeValue):
	if rootNode.data==nodeValue:
		return "Found"
	elif rootNode.data >nodeValue:
			if rootNode.left.data ==nodeValue:
				return "Found"
			else:
				search(rootNode.left,nodeValue)
	else:
		if rootNode.right.data==nodeValue:
			return "Found"
		else:
			search(rootNode.right,nodeValue)
	return "Not Found"

