#main operation of LL
# insert, traverse, delete, search
# insert:-- head , tail(append) , middle(insert)
#traverse:-- print
#delete:-- head, tail(pop), value (remove) , index
#search:-- value, index

#--- insert form head

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

L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(len(L))