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
        ptr=self.head
        while ptr.next!=None:
            ptr=ptr.next
        ptr.next=newNode
    def print(self):
        ptr=self.head
        while ptr.next!=None:
            print(ptr.data,"->")
            if ptr.next==None:
                print("End")
            ptr=ptr.next
            
linked_list=LinkedList()
# linked_list.insert(10)
# linked_list.insert(20)
# linked_list.insert(30)
arr=[10,20,30,40,50]
for i in arr:
    linked_list.insert(i)
linked_list.print()
print("done")