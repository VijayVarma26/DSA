# Stack Class with required Functions
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
    


# Testing
s = Stack()

print(s.isEmpty())

s.push("Vijay")
s.push(1)
s.push(2)
s.push(True)

print(s.pop())

print(s.isEmpty())

print(s.peek())



