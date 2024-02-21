class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None #empty linkedlist
        self.n = 0 #number of node
    
    def __len__(self):
        return self.n

L = Linkedlist()
print(L)
print(len(L))