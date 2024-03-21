class Queue:
    def __init__(self):
        self.size=5
        self.rear=-1
        self.front=-1
        self.list=[0]*self.size
    def isFull(self):
        if self.rear==self.size-1:
            return True
        else:
            return False
    def isEmpty(self):
        if self.rear==-1 and self.front==-1:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isFull():
            print("OverFlow")
        if self.isEmpty():
            self.rear=0
            self.front=0
            self.list[self.rear]=value
        else:
            self.rear+=1
            self.list[self.rear]=value
    def dequeue(self):
        if self.isEmpty():
            print("UnderFlow")
        self.list[self.front]=None
        self.front+=1
    def status(self):
        if self.isEmpty():
            print("Queue is Empty")
        print("front->",end=" ")
        for i in range(self.front,self.rear+1):
            print(self.list[i],"->",end=" ")
        print("rear")
q=Queue()
# while True:
#     print("1.Inserting Element In The Queue")
#     print("2.Removing Element In The Queue")
#     print("3.Check The Queue is Full")
#     print("4.Check The Queue is Empty")
#     print("5.Find the Status of The Queue")
#     print("6.Exit")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         value=int(input("Enter the value to be Inserted"))
#         q.enqueue(value)
#     if choice==2:
#         q.dequeue()
#     if choice==3:
#         print(q.isFull())
#     if choice==4:
#         print(q.isEmpty())
#     if choice==5:
#         q.status()
#     if choice==6:
#         break
#     print("--------------***---------------")
# print("DONE")
    
                        
            
        