class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def display(self):
        disp = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            disp.append(cur.data)
        print(disp)

l = LL()
l.head = Node(11)
element2 = Node(22)
element3 = Node(33)

l.head.next = element2
element2.next = element3
l.display()