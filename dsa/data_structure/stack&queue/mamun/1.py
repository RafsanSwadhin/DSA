class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        return item
    
    def is_empty(self):
        #if len(self.stack) == 0:
         #   return True
        #else:
            #return False
        return len(self.stack) == 0
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    
    def peak(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack[-1]
    
s = Stack()
s.push(555)
s.push(10)
s.push(11)
s.push(22)
s.push(16)
print('Now I am adding',s.push(33))
print("My stack is :",s.stack)
print(s.size())
print(s.peak())
print(s.pop())
print(s.peak())
