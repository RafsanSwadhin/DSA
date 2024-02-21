class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):        
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
           last_node = last_node.next
        last_node.next = new_node

ll = LinkedList()
ll.append(5)
ll.append(4)
ll.append(7)
ll.print_list()