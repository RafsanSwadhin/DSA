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

print(_1stNode) #<__main__.Node object at 0x00000143F2021450>
print(int(0x00000143F2021450))
print(_1stNode.data) #A
print(_1stNode.next) #None