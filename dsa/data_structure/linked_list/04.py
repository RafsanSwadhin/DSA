# traverse

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
    
    def insert_head(self,value): #value = insert_value
        #new node
        new_node = Node(value) # new_node = object of Node class
        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        #increment n
        self.n = self.n + 1
    
    def traverse(self):
        curr = self.head

        while curr is not None:
        #while curr != None:
        #while curr:
            print(curr.data)
            curr = curr.next
    
    # if u want to print like this = 1->2->3->4
    
    def __str__(self):
        curr = self.head
        result = ""
        while curr is not None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2] #-- this is bcz last '->' will not be printed

        
L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.traverse()
print(L)


