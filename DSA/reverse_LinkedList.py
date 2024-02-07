class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=Node(data)
        if self.head ==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
    def reverse(self):
        prev=None
        current=self.head
        nex=self.head
        if self.head==None:
            return self.head
        while current!=None:
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        return prev
    def print(self,pointer):
        ptr=pointer
        while ptr!=None:
            print(ptr.data)
            ptr=ptr.next
obj=LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(7)
obj.insert(40)
obj.insert(100)
print("before reversiing")
obj.print(obj.head)
print("after reverse")
obj.print(obj.reverse())