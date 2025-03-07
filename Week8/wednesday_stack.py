class Stack:
    def __init__(self) -> None:
        self.items = []

    # implement the push() operation
    def push(self, item):
        self.items.append(item) 

    # implement the pop() operation
    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    # implement the peek() operation
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    # implement the getting size() operation
    def size(self):
        return len(self.items)

    # implement checking is_empty() operation
    def is_empty(self):
        return self.items == []
    
