class queue:
	def __init__(self):
		self.list=[]
	def enqueue(self,value):
		self.list.append(value)
	def dequeue(self):
		value=self.list.pop(0)
		return value
	def isEmpty(self):
		if len(self.list)==0:
			return True
		else:
			return False
	def __str__(self):
		return f"{self.list}"