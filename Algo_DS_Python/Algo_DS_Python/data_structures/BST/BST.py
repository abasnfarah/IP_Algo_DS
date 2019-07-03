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
from Algo_DS_Python.data_structures.queue.queue import ListQueue
import sys
# Class For BST 
# Methods for class :
#   isEmpty, find, findMin, findmax, insert, delete, height, 
# Functions
#   getSize, height, [inorder, preorder, postorder traversal] 

# Node with a value and right and left children
class Node:
    def __init__(self, val):
        self.val = val
        #self.key = key
        self.right= None
        self.left= None

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
        if( val > tree.val):
            if(tree.right == None):
                tree.right = Node(val)
            else:
                self.insertWrapper(tree.right, val)
        else:
            if(tree.left == None):
                tree.left = Node(val)
            else:
                self.insertWrapper(tree.left, val)

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
            if(ptr.val == val):
                return True
            else:
                ptr = ptr.right if ptr.val < val else ptr.left
        return False

# This Prints the Tree Using In-Order-Traversal
def printTree(root):
    if (root!= None):
        printTree(root.left)
        print(root.val)
        printTree(root.right)

# This function find the min element in BST
def findMin(tree):
    root = tree.getTree()
    if(root == None):
        print("ERROR: The tree is empty")
        return None
    while(root.left != None):
        root = root.left

    return root.val

# This funciton finds the max element in BST
def findMax(tree):
    root = tree.getTree()
    if(root == None):
        print("Error: The tree is empty")
        return None
    while(root.right != None):
        root = root.right

    return root.val

# This gets the root node out of BST then runs function
def findHeight(tree):
    root = tree.getTree()
    return findHeightRecursive(root)

# This function finds a height of a tree using recursion
def findHeightRecursive(root):
    if(root == None):
        return -1

    rightHeight = findHeightRecursive(root.right)
    leftHeight = findHeightRecursive(root.left)

    return max(rightHeight, leftHeight) + 1

# This a BredthFirstSearch traversal printing every element tree by height
def levelOrderTraversal(tree):
    root = tree.getTree()
    nodeQueue = ListQueue(root)

    # Ends once queuue is empty and tree has been traversed
    while(nodeQueue.isEmpty() == False):
        ptr = nodeQueue.dequeue()
        if(ptr.left != None and ptr.right != None):
            nodeQueue.enqueue(ptr.left)
            nodeQueue.enqueue(ptr.right)
        if(ptr.left != None and ptr.right == None):
            nodeQueue.enqueue(ptr.left)
        elif(ptr.right != None and ptr.left == None):
            nodeQueue.enqueue(ptr.right)
        print(ptr.val)

# These next three funcitons are different Depth-first Search traversals

# Preorder Traversal gets the roots value then traverses the right sub tree then left subtree
def preorder(root):
    if(root != None):
        print(root.val)
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if(root != None):
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def inorderList(root):
    if(root == None):
        return [None]
    L = inorderList(root.left)
    R = inorderList(root.right)
    if(L == [None] and R == [None]):
        return [root.val]
    elif(L == [None] and R != [None]):
        return [root.val] + R
    elif(L != [None] and R == [None]):
        return L + [root.val]
    else:
        return L + [root.val] + R
def postorder(root):
    if(root != None):
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# This function takes a root Node as imput and checks if it is a BST following the given invariant
# That the left subtree L rooted at R is less then R.val and the right subtree is greater then R.val
# This uses isSubtreeLesser and isSubtreeGreater as subroutines
def isBinaryTree(root):
    outputBoolean = True
    if(root != None):
        nodeList = inorderList(root)
        x = -sys.maxsize

        for i in range(0, len(nodeList)):
            if(x < nodeList[i]):
                x = nodeList[i]
            else:
                outputBoolean = False

    return outputBoolean

