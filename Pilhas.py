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

MyStack = stack()

MyStack.push("Pagina 1")
MyStack.push("Pagina 2")
MyStack.push("Pagina 3")
MyStack.push("Pagina 4")

print(MyStack.items)

MyStack.pop()
MyStack.pop()

print(MyStack.items)