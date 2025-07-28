#Binary Search Tree 
#A Binary Search Tree is a type of binary tree where each node has at most two children, and the tree maintains a specific order:

'''For any node:

    Left child contains values less than the node.

    Right child contains values greater than the node.'''
    
    
'''Why Do We Use BST in Programming?
BSTs are widely used because they:

    Provide fast search, insert, and delete operations (average case: O(log n)).

    Keep data in a sorted structure.

    Are useful in scenarios where dynamic set operations (like add/remove/search) are needed.'''
    
#Common Operations in a Binary Search Tree
'''
    Operation	                        Description
Insert	            ->        Add a node while maintaining BST properties
Search / Find	    ->        Locate a node with a specific value
Delete	            ->        Remove a node, then re-balance the tree to preserve BST structure
Traversal	        ->        Visit all nodes (in-order, pre-order, post-order, level-order)
Find Min/Max	    ->        Get the smallest or largest value in the tree
Height / Depth	    ->        Compute the tree's height (longest path from root to leaf)
Check Validity	    ->        Verify whether a binary tree satisfies BST properties
Find Successor	    ->        Find the next higher value node (in-order successor)
Find Predecessor	->        Find the next lower value node (in-order predecessor)'''
    
    
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else: #key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    # Search a node
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    # In-order Traversal (sorted order)
    def in_order(self):
        self.in_order_traversal(self.root)
        print()

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.key, end=" ")
            self.in_order_traversal(node.right)

    # Find minimum value
    def find_min(self):
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current.key

    # Find maximum value
    def find_max(self):
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.key


bst = BST()     
elements = [1,3,2,4,6,5,8,7]

for ele in elements:
    bst.insert(ele)
    

print("Found"if bst.search(8) else "Not Found")
print("Found"if bst.search(80) else "Not Found")

bst.inorder()

print("Max Number:",bst.find_max())
print("Min Number:",bst.find_min())


