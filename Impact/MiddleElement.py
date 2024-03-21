class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
	def insertLast(self,value):
		node=Node(value)
		if self.head==None:
			self.head=node
		else:
			ptr=self.head
			while ptr.next!=None:
				ptr=ptr.next
			ptr.next=node
	def insert
	def print(self):
		ptr=self.head
		while ptr!=None:
			print(ptr.data,"->",end="")
			ptr=ptr.next
			if ptr==None:
				print("None")
	def middleElement(self):
		ptr=self.head
		preptr=self.head
		while ptr!=None:
			preptr=ptr
			ptr=ptr.next.next
		print(preptr.data)
ll=LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.print()
ll.middleElement()