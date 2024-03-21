class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.next!=None:
                ptr=ptr.next
            ptr.next=newNode
    def printf(self):
        ptr=self.head
        string=""
        while ptr!=None:
            print(ptr.data,end="->")
            ptr=ptr.next
        print("End")
    def search(self,data):
        if self.head is None:
            return -1
        ptr=self.head
        i=0
        while ptr!=None:
            if ptr.data==data:
                return i
            i+=1
            ptr=ptr.next
        return -1
    def delete(self,data):
        ptr=self.head
        preptr=self.head
        while ptr!=None:
            preptr=ptr
            ptr=ptr.next
            if ptr.data==data:
                preptr.next=ptr.next
                return "Deleted"
        return "Not Deleted"
    def insertFirst(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def deleteEnd(self):
        preptr=None
        ptr=self.head
        if self.head.next ==None:
            pass
        while preptr!=None:
            preptr=ptr
            ptr=ptr.next
        preptr.next=None
    def sort(self):
        ptr=self.head
        while ptr!=None:
            preptr=self.head
            while preptr.next!=None:
                if preptr.data>preptr.next.data:
                    preptr.data,preptr.next.data=preptr.next.data,preptr.data
                preptr=preptr.next
            ptr=ptr.next
    def length(self):
        ptr=self.head
        n=0
        while ptr!=None:
            ptr=ptr.next
            n+=1
        return n
    def insertMidle(self,data):
        if self.head==None:
            return "No Element"
        newNode=Node(data)
        size=self.length()//2
        ptr=self.head
        print(size)
        for _ in range(size-1):
            ptr=ptr.next
        temp=ptr.next.next
        ptr.next=newNode
        newNode
        

ll=LinkedList()
array=list(map(int,input().split()))
for i in range(len(array)):
    ll.append(array[i])

searchValue=int(input("Enter the vaue to be searched"))

found=ll.search(searchValue)
if found==-1:
    print("Not Found")
else:
    print("Found at the index ",found)
ll.printf()

