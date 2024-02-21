class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

_1stNode = Node("A")
_2ndNode = Node("D")
_3rdNode = Node("C")
_4thNode = Node("F")
_5thNode = Node("E")
_6thNode = Node("B")

print(_1stNode.data) #A
print(_1stNode.next) #None
_1stNode.next = _2ndNode
print(_1stNode.next.data)
print(_2ndNode.data)
