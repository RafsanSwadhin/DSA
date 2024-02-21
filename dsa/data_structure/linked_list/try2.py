# traverse

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # empty linked list
        self.n = 0  # number of nodes

    def __len__(self):
        return self.n

    def insert_end(self, value):  # value = insert_value
        # new node
        new_node = Node(value)  # new_node = object of Node class

        if not self.head:
            # if the list is empty, make the new node the head
            self.head = new_node
        else:
            # otherwise, find the last node and make it point to the new node
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        # increment n
        self.n += 1

    def traverse(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next

L = LinkedList()
L.insert_end(1)
L.insert_end(2)
L.insert_end(3)
L.insert_end(4)
L.traverse()
