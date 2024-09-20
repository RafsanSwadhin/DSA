'''
        13
       /  \
     10    15
    / \   /  \
   5  12  14  20
'''
#in-order traversal
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse_in_order(root):
    if root:
        traverse_in_order(root.left)  # Traverse the left subtree
        print(root.val)               # Visit the root node
        traverse_in_order(root.right) # Traverse the right subtree

def main():
    root = TreeNode(13)
    root.left = TreeNode(10)
    root.right = TreeNode(15)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(12)

    root.right.left = TreeNode(14)
    root.right.right = TreeNode(20)

    traverse_in_order(root)  # Perform in-order traversal

main()
