class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        if len(self.stack)==0:
            return "UnderFlow"
        return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return "No Elements in the Stack"
        return self.stack[-1]
    def display(self):
        if len(self.stack)==0:
            return "no elements in the Stack"
        print(self.stack)
st=Stack()
st.push(10)
st.push(20)
st.push(30)
print("The top of the Stack",st.peek())
print("The elements in the list")
st.display()
st.pop()
print("After popping the last element")
st.display()
# {[()]}


        