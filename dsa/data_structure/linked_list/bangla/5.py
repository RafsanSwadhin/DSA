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
    
    def prepend(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


ll = LinkedList()
ll.append(5)
ll.append(4)
ll.append(7)
ll.prepend(55)
ll.print_list()

"""
Certainly! Let's break down the `prepend` method:

```python
def prepend(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
```

1. **Create a New Node:**
   ```python
   new_node = Node(new_data)
   ```
   - A new node is created with the specified `new_data` (in this case, 55).

2. **Set the Next of the New Node:**
   ```python
   new_node.next = self.head
   ```
   - The `next` attribute of the new node is set to the current `head` of the linked list.
   - This step is crucial because it preserves the existing structure of the list.

3. **Update the Head of the Linked List:**
   ```python
   self.head = new_node
   ```
   - The `head` of the linked list is updated to point to the new node.
   - Now, the new node becomes the first element in the linked list.

Let's visualize the process:

- Initially, the linked list is `[5 -> 4 -> 7]` with `head` pointing to the node with data 5.
- After calling `prepend(55)`, a new node `[55 -> None]` is created.
- The `next` of the new node is set to the current `head`, resulting in `[55 -> 5 -> 4 -> 7]`.
- Finally, the `head` of the linked list is updated to the new node, making it the first element: `[55 -> 5 -> 4 -> 7]`.

So, the `prepend` method adds a new node with the specified data to the beginning of the linked list, and it becomes the new head of the list.
"""