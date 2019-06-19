"""
     This is the class definition for a AVL_BST (Adelson-Velsky-Landis Binary Search Tree)
     INVARIANT: all elements in the right sub tree are < root and all elements in the left sub tree are > then the root node. Also, for every node the left and right children's heights differ by at most +-1.

     This BST maintains a balanced structure using rotations.
     Sample BST's:
            Perfect Balanced                non-Perfect Balanced AVL Tree
                    4                                 4
                /       \                         /     \
              2          6                       2       6
             / \        / \                     / \
           1    3      5   7                   1   3
"""

#Methods for AVL_BST class==> Insert, Right-Rotate, left-rotate, AVL_Sort
from BST.BST import Node, BST, printTree
#importing Copy for compy operations
import copy

class AVL_Node(Node):
    def __init__(self, val, parent=None, isLeft=None):
        Node.__init__(self, val)
        self._parent = parent
        self._height = 0
        self._isLeft = isLeft

    # Getter and setter for height atribute
    def getHeight(self):
        return self._height

    def setHeight(self, height):
        self._height = height

    def isLeft(self):
        return self._isLeft

    def setIsLeft(self, isLeft):
        self._isLeft = isLeft

    #Getter and Setters for parent attribute
    def getParent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = parent

    #Overiding Setter variables from parent class
    def setRight(self, right):
        self._right = right

    def setLeft(self, left):
        self._left = left


class AVL_BST(BST):
    def __init__(self, val=None):
        self.tree = None if val is None else AVL_Node(val)

    def setTree(self, tree):
        self.tree = tree

    def balanceHeights(self, tree):
        if(tree.getRight() != None and tree.getLeft() != None):
            tree.setHeight(1 + max(tree.getLeft().getHeight(), tree.getRight().getHeight()))
        elif(tree.getRight() != None and Tree.getLeft() == None):
            tree.setHeight(1 + tree.getRight().getHeight())
        elif(tree.getRight() == None and Tree.getLeft() != None):
            tree.setHeight(1 + tree.getLeft().getHeight())
        else:
            tree.setHeight(0)


    #This rotates a sub tree to the left
    def leftRotate(self, x):

        # Rotation Step
        # Doing shallow copy so changes on y reflect on x.Left
        y = copy.copy(x.getRight())
        x.setRight(y.getLeft())
        y.setLeft(x)

       # Set New Heights now
        self.balanceHeights(x)
        self.balanceHeights(y)

        # Updating the state of X and Y
        if(x.getParent() != None):
            y.setParent(x.getParent())
            y.setIsLeft(x.isLeft())
            parent = copy.copy(y.getParent())
            if(y.isLeft() == True):
                parent.setLeft(y)
            else:
                parent.setRight(y)
        else:
            y.setParent(None)
            y.setIsLeft(None)

        x.setParent(y)
        x.setIsLeft(True)

        b = copy.copy(x.getRight())
        if(b != None):
            b.setIsLeft(False)
            b.setParent(x)

        return y


    def rightRotate(self, x):
        # Rotation Step
        # Doing shallow copy so changes on y reflect on x.Left
        y = copy.copy(x.getLeft())
        x.setLeft(y.getRight())
        y.setRight(x)

       # Set New Heights now
        self.balanceHeights(x)
        self.balanceHeights(y)

        # Updating the state of X and Y
        if(x.getParent() != None):
            y.setParent(x.getParent())
            y.setIsLeft(x.isLeft())
            parent = copy.copy(y.getParent())
            if(y.isLeft() == True):
                parent.setLeft(y)
            else:
                parent.setRight(y)
        else:
            y.setParent(None)
            y.setIsLeft(None)

        x.setParent(y)
        x.setIsLeft(False)

        b = copy.copy(x.getLeft())
        if(b != None):
            b.setIsLeft(True)
            b.setParent(x)

        #changing x to y so not suck in sub directory
        return y

    # This is a overwriting function to insert AVL_Nodes 
    # in this class vs Nodes from BST Parent class
    def insertWrapper(self, tree, val):
        if( val > tree.getVal()):
            if(tree.getRight() == None):
                tree.setRight(AVL_Node(val, tree, False))
            else:
                self.insertWrapper(tree.getRight(), val)
        else:
            if(tree.getLeft() == None):
                tree.setLeft(AVL_Node(val, tree, True))
            else:
                self.insertWrapper(tree.getLeft(), val)

    # this takes O(height) time to insert as well due to binary 

    def insert(self, val):
        if(self.tree == None):
            self.tree = AVL_Node(val)
        else:
            self.insertWrapper(self.tree, val)

def main():
    tree = AVL_BST(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(6)
    tree.insert(5)
    tree.insert(7)
    tree.setTree(tree.rightRotate(tree.getTree()))
    printTree(tree.getTree())

main()
