class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
            newNode.prev=ptr
    def printf(self):
        ptr=self.head
        while ptr!=None:
            print(ptr.data,end="->")
            ptr=ptr.next
        