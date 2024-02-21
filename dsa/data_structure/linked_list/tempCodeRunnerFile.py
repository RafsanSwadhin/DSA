class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None  # empty linkedlist
        self.n = 0  # number of nodes

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def __str__(self):
        curr = self.head
        result = ""
        while curr is not None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]

    def append(self, value):
        new_node = Node(value)
        if not self.head :
            self.head = new_node
            self.n += 1
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        self.n += 1

# Example usage:
L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.traverse()
print(L)
L.append(5)
print(L)
