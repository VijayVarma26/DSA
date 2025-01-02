# Implementing Queue Data Structure 
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    

#  Testing Queue Implemntation

# Create Queue object
q = Queue()

# Adding Elements in the queue (Enqueue)
q.enqueue(12)
q.enqueue("Vijay")
q.enqueue("Varma")
q.enqueue(False)

# Removing Elements from the queue (Dequeue)
print(q.dequeue())
print(q.dequeue())

# Checking is empty
print(q.isEmpty())

# Checking size
print(q.size())

