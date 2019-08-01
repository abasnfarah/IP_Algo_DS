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

import sys
import os
# Using Queue python implementation
# Getting directory of script being run
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append('.')
# Adding dependency module to our python PATH
sys.path.append(dirpath + '/../..')
print(sys.path)
from data_structures.queue.queue import ListQueue

# Class For BST 
# Methods for class :
#   isEmpty, find, findMin, findmax, insert, delete, height, 
# Functions
#   getSize, height, [inorder, preorder, postorder traversal] 

# Node with a value and right and left children
class Node:
    def __init__(self, val, parent=None):
        self.val = val
        #self.key = key
        self.right= None
        self.left= None
        self.parent = None

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

    # this returns the element once found
    def getFind(self, val):
        ptr = self.tree
        while(ptr != None):
            if(ptr.val == val):
                return ptr
            else:
                ptr = ptr.right if ptr.val < val else ptr.left

        # if ptr is None then element doesn't exist in BST
        return None

    # This returns a Node that is the max element in this tree
    def findMax(self, node):
        if(node == None):
            return None
        elif(node.right == None):
            return node
        else:
            return self.findMax(node.right)

    # This takes in a node and drills it's subtree to find minimim element in tree
    def findMin(self, node):
        if(node == None):
            return None
        elif(node.left == None):
            return Node
        else:
            return self.findMax(node.left)


    # This deletes a certain node if it finds the data 
    # This uses three cases
    # Case 1: if node to be deleted has no child, then just change it to None
    # Case 2: if node to be deleted has one child then just change link from parent to it's child node
    # Case 3 if node to be deleted has two children then will find max in left and copy the value in targetted node. Then delete duplicate
    def delete(self, val):
        self.tree = self.deleteUtil(self.tree, val)

    def deleteUtil(self, root, val): 
        if(root == None):
            return root
        elif(val < root.val):
            root.left = self.deleteUtil(root.left, val)
        elif(val > root.val):
            root.right = self.deleteUtil(root.right, val)
        else:
            # case 1: No child
            if ( root.left == None and root.right == None):
                root = None
            # case 2: One child
            elif( root.right == None):
                root = root.left
            elif(root.left == None):
                root = root.right
            # case 3: Two children
            else:
                temp = self.findMax(root.left)
                root.val= temp.val
                root.left = self.deleteUtil(root.left, temp.val)

        return root

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

    return root

def findMinNode(root):
    if(root == None):
        print("ERROR: The tree is empty")
        return None
    while(root.left != None):
        root = root.left

    return root


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

# These two functions takes a root Node as imput and checks if it is a BST following the given invariant
# That the left subtree L rooted at R is less then R.val and the right subtree is greater then R.val

# This uses inorder traversal and puts elements in an array. If the array isn't sorted then it is not a BST
def isBinarySearchTreeInorder(root):
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

# This traverses the Tree using upper and lower limits to see if the node fits in the limit
# If the node doesn't fall within the limit then the BST isn't a BST
def isBinarySearchTree(root):
    return isBSTUtil(root.getTree(), -sys.maxsize -1, sys.maxsize)

def isBSTUtil(root, minValue, maxValue):
    if (root == None):
        return True
    elif( root.val > minValue and root.val < maxValue
            and isBSTUtil(root.left, minValue, root.val)
            and isBSTUtil(root.right, root.val, maxValue)):
        return True
    else:
        return False

# The running time of this algorithm is O(h) where h is the height of tree
# If tree is balanced the running time is O(Lgn)
def inOrderSuccessor(root, val):
    # Need to find the node to compare
    current = root.getFind(val)
    if(current == None):
        return None
    # Case 1 Node has right subtree
    if(current.right != None):
        return findMinNode(current.right)
    else:
        successor = None
        ancestor = root.getTree()
        while(ancestor != current):
            if(current.val < ancestor.val):
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor















