class stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.size()==0:
            return None
        else:
            self.items.pop()

class Queue:
    def __init__(self):
        self.instorage = stack()
        self.outstorage = stack()
    def size(self):
        return self.instorage.size() + self.outstorage.size()
    def enqueue(self, items):
        self.instorage.push(items)
    def dequeue(self):
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()
    
q = Queue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)



# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
