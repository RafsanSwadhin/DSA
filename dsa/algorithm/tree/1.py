
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

def traverse(root):
    if root:
        print(root.val)
        traverse(root.left)
        traverse(root.right)

def main():
    root = TreeNode(13)
    root.left = TreeNode(10)
    root.right = TreeNode(15)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(12)

    root.right.left = TreeNode(14)
    root.right.right = TreeNode(20)

    traverse(root)

main()
