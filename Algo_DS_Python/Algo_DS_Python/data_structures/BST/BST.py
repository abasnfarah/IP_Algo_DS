"""
     This is the class definition for a BST (Binary Search Tree)
     INVARIANT: all elements in the right sub tree are < root and all elements in the left sub tree are > then the root node.

     Sample BST's:
                Balanced                Non Balanced Worst Case BST
                    4                               1
                /       \                            \
              2          6                            2
             / \        / \                            \
           1    3      5   7                            3
"""

# Class For BST 
# Methods for class :
#   isEmpty, find, findMin, findmax, insert, delete, height, 
# Functions
#   getSize, height, [inorder, preorder, postorder traversal] 

# Node with a value and right and left children
class Node:
    def __init__(self, val):
        self._val = val
        #self.key = key
        self._right= None
        self._left= None

    # Getter and Setters
    def getVal(self):
        return self._val

    def getRight(self):
        return self._right

    def getLeft(self):
        return self._left

    def setVal(self, val):
        self._val = val

    def setRight(self, right):
        self._right = right

    def setLeft(self, left):
        self._left = left

class BST:
    tree = None
    def __init__(self, val=None):
        self.tree = None if val is None else Node(val)

    def isEmpty(self):
        if(self.tree == None):
            return True
        else:
            return False

    def getTree(self):
        return self.tree

    # This is a wrapper function that takes in just the val
    def insertWrapper(self, tree, val):
        if( val > tree.getVal()):
            if(tree.getRight() == None):
                tree.setRight(Node(val))
            else:
                self.insertWrapper(tree.getRight(), val)
        else:
            if(tree.getLeft() == None):
                tree.setLeft(Node(val))
            else:
                self.insertWrapper(tree.getLeft(), val)

    # this takes O(height) time to insert as well due to binary 
    def insert(self, val):
        if(self.tree == None):
            self.tree = Node(val)
        else:
            self.insertWrapper(self.tree, val)

    # This follows the left and right pointers till it finds the val
    # Complexity is O(H) where H is the height of the tree
    def find(self, val):
        ptr = self.tree
        while(ptr != None):
            if(ptr.getVal() == val):
                return True
            else:
                ptr = ptr.getRight() if ptr.getVal() < val else ptr.getLeft()
        return False

# This Prints the Tree Using In-Order-Traversal
def printTree(tree):
    if (tree != None):
        printTree(tree.getLeft())
        print(tree.getVal())
        printTree(tree.getRight())

