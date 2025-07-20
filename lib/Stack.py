class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        

    def isEmpty(self):
        return  len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        

        return self.items
        

    def pop(self):
        
        return None if self.isEmpty() else self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)
        

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        
        try:
            return len(self.items) - self.items.index(target) - 1 
        except ValueError:
            return -1


if __name__ == "__main__":
    stk = Stack([5,6,7,8,9,10],)
    print(stk.search(5))



