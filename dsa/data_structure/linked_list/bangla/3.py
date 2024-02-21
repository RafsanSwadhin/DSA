class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next


# creating object
_1stNode = Node("A")
_2ndNode = Node("D")
_3rdNode = Node("C")
_4thNode = Node("F")
_5thNode = Node("E")
_6thNode = Node("B")
print("nodes")
print(_1stNode)
print(_2ndNode)
print(_3rdNode)
print(_4thNode)
print(_5thNode)
print(_6thNode)
print()
print("data")
print(_1stNode.data) #A
print(_2ndNode.data) #D
print(_3rdNode.data) #C
print(_4thNode.data) #F
print(_5thNode.data) #E  
print(_6thNode.data) #B

_1stNode.next = _2ndNode
_2ndNode.next = _3rdNode
_3rdNode.next = _4thNode
_4thNode.next = _5thNode
_5thNode.next = _6thNode
print("After making link")
print(_1stNode.next)
print(_2ndNode.next)
print(_3rdNode.next) #_4thNode
print(_4thNode.next) # _5thNode
print(_5thNode.next) # _6thNode
print(_6thNode.next)