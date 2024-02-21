class Node:    #the programmer in you
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) :
        self.head = None

    def insert(self,newNode):
        # head = Rafsan-> None
        if self.head is None:
            self.head = newNode
        # head = Rafsan -> Jani -> None
        else: 

            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next 
            lastNode.next = newNode
    
    def printlist(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next 

# Create nodes
firstNode = Node("rafsan")
secondNode = Node("jani")
thirdNode = Node("ahmed")

# Create a linked list
LL = LinkedList()

# Insert nodes into the linked list
LL.insert(firstNode)
LL.insert(secondNode)
LL.insert(thirdNode)

# Print the linked list
LL.printlist()