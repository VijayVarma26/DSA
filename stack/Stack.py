# Stack Implementation Code 
class Stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    

# Testing Stack Implementation

# Creating Stack Object
s = Stack()

# Checking if stack is empty
print(s.isEmpty())

# Pushing Elements in the Stack
s.push("Vijay")
s.push(1)
s.push(2)
s.push(True)

# Poping elements from stack
print(s.pop())

# Checking the top element of the stack 
print(s.peek())



