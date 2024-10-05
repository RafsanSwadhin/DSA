class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
             node.right = self.insert(node.right,data)
        return node
    
"""

Let's break down how the given list of values `[5, 2, 10, 7, 15, 12, 20, 30, 6, 8]` will be inserted into your binary search tree (BST) using your provided `Node` and `Tree` classes.

### Step-by-Step Explanation:

You have a list: `[5, 2, 10, 7, 15, 12, 20, 30, 6, 8]`. These numbers will be inserted into the tree one by one following the rules of a binary search tree:
1. If the value to be inserted is smaller than the current node, go to the left child.
2. If the value is larger than or equal to the current node, go to the right child.

### Starting the Tree:

- **Insert 5:**
  - The tree is initially empty (`root` is `None`), so we insert `5` as the root node.
  
  ```
        5
       / \
     None None
  ```

- **Insert 2:**
  - Compare `2` with the root (`5`). Since `2` is less than `5`, we insert `2` as the left child of `5`.

  ```
        5
       / \
      2  None
     / \
  None None
  ```

- **Insert 10:**
  - Compare `10` with `5`. Since `10` is greater than `5`, we insert `10` as the right child of `5`.

  ```
        5
       / \
      2   10
     / \  / \
  None None None None
  ```

- **Insert 7:**
  - Compare `7` with `5`. Since `7` is greater than `5`, we go to the right child (`10`).
  - Compare `7` with `10`. Since `7` is less than `10`, we insert `7` as the left child of `10`.

  ```
        5
       / \
      2   10
         / \
        7  None
       / \
    None None
  ```

- **Insert 15:**
  - Compare `15` with `5`. Since `15` is greater than `5`, we go to the right child (`10`).
  - Compare `15` with `10`. Since `15` is greater than `10`, we insert `15` as the right child of `10`.

  ```
        5
       / \
      2   10
         /  \
        7    15
       / \   / \
    None None None None
  ```

- **Insert 12:**
  - Compare `12` with `5`, `10`, and `15`. Since `12` is greater than `10` but less than `15`, we insert `12` as the left child of `15`.

  ```
        5
       / \
      2   10
         /  \
        7    15
            /  \
           12  None
          / \
       None None
  ```

- **Insert 20:**
  - Compare `20` with `5`, `10`, and `15`. Since `20` is greater than all of them, we insert `20` as the right child of `15`.

  ```
        5
       / \
      2   10
         /  \
        7    15
            /  \
           12   20
               /  \
            None  None
  ```

- **Insert 30:**
  - Compare `30` with `5`, `10`, `15`, and `20`. Since `30` is greater than all of them, we insert `30` as the right child of `20`.

  ```
        5
       / \
      2   10
         /  \
        7    15
            /  \
           12   20
                  \
                  30
                 /  \
              None  None
  ```

- **Insert 6:**
  - Compare `6` with `5`, `10`, and `7`. Since `6` is greater than `5` but less than `10` and `7`, we insert `6` as the left child of `7`.

  ```
        5
       / \
      2   10
         /  \
        7    15
       / \   / \
      6  None 20
          / \
       None  30
           /  \
        None  None
  ```

- **Insert 8:**
  - Compare `8` with `5`, `10`, and `7`. Since `8` is greater than `5` and `7`, but less than `10`, we insert `8` as the right child of `7`.

  ```
        5
       / \
      2   10
         /  \
        7    15
       / \   / \
      6   8  12 20
              /   \
             None  30
                  /  \
               None  None
  ```

### Final Tree Structure:

After inserting all the values `[5, 2, 10, 7, 15, 12, 20, 30, 6, 8]`, the final tree looks like this:

```
        5
       / \
      2   10
         /  \
        7    15
       / \   / \
      6   8 12  20
                 \
                 30
```

### How Insertion Works in the Code:
1. **`insert(self, node, data)`**:
   - The method first checks if the `node` is `None`. If it is, a new node is created.
   - If `data` is less than `node.data`, the function goes down the left subtree.
   - If `data` is greater than or equal to `node.data`, it goes down the right subtree.
   - Recursion continues until the correct position is found for the new node.



"""