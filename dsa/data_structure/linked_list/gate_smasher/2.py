# Node class for a linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data held by the node
        self.next = None  # Pointer to the next node (initially None)

# Creating nodes with data
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4

# Head points to the first node of the list
head = node1

# Function to traverse and display the linked list
def print_linked_list(head):
    current = head  # Start from the head node
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")  # End of the list

print("Original linked list:")
print_linked_list(head)  # Display the linked list before insertion

# Insertion at the beginning of the linked list
new_node = Node(50)  # Create a new node with data
new_node.next = head  # Point the new node's next to the current head
head = new_node       # Update the head to the new node

print("\nLinked list after insertion at the beginning:")
print_linked_list(head)  # Display the linked list after insertion




''' 
current =  node1
while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")
'''



