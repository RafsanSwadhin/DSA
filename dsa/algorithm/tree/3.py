'''
        13
       /  \
     10    15
    / \   /  \
   5  12  14  20
'''
#pre-order traversal
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse_post_order(root):
    if root:
        traverse_post_order(root.left)  # Traverse the left subtree
        traverse_post_order(root.right) # Traverse the right subtree
        print(root.val)                 # Visit the root node

def main():
    root = TreeNode(13)
    root.left = TreeNode(10)
    root.right = TreeNode(15)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(12)

    root.right.left = TreeNode(14)
    root.right.right = TreeNode(20)

    traverse_post_order(root)  # Perform post-order traversal

main()
