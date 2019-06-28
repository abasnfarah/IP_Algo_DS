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

#importing Copy for compy operations
import copy

class AVL_Node(): 
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.height = 0

class AVL_BST():

    def __init__(self, val=None):
        self.tree = None if val is None else AVL_Node(val)

    def getTree(self):
        return self.tree

    def heightIfExists(self, node):
        if node is None:
            return -1
        else:
            return node.height

    # This method gets the new height of parent based off children heights 
    def newHeight(self, node):
        l = self.heightIfExists(node.left)
        r = self.heightIfExists(node.right)

        return max(l,r) + 1

    def getDifference(self, node):
        l = self.heightIfExists(node.left)
        r = self.heightIfExists(node.right)

        return abs(l - r)

    # This function returns 0 if left heavy and 1 if right Heavy and -1 if equal
    def rightOrLeftHeavy(self, root):
        if(root == None):
            return -1
        else:
            # need childrens heights

            l = self.heightIfExists(root.left)
            r = self.heightIfExists(root.right)

            if l == r:
                return -1
            elif( l > r):
                return 0
            else:
                return 1

    # This does a right Rotation of sub trees at root x
    def right_Rotation(self, x):
        y = x.left
        b = y.right

        # Rotating Variables
        y.right = x
        x.left = b

        #Updating Heights
        x.height = self.newHeight(x)
        y.height = self.newHeight(y) 

        return y

    def left_Rotation(self, x):
        y = x.right
        b = y.left

        # rotating
        y.left = x
        x.right = b

        #updating Heights
        x.height = self.newHeight(x)
        y.height = self.newHeight(y)

        return y


    def wInsert(self, root, val):

        # The actual inserting just like our BST Class
        # base case
        if(root == None):
            root = AVL_Node(val)
        elif((val > root.val) and root.right == None):
            root.right = AVL_Node(val)
        elif((val > root.val) and root.right != None):
            self.wInsert(root.right, val)
        elif((val < root.val) and root.left == None):
            root.left = AVL_Node(val)
        elif((val < root.val) and root.left != None):
            self.wInsert(root.left, val)

        # now need to reGet Height after insert
        root.height = self.newHeight(root)

        # Getting differences of sub tree heights and if root is right or left heavy
        d = self.getDifference(root)
        h = self.rightOrLeftHeavy(root)

        # now we have four cases to rotate, 1.left, 2.right, 3.leftRight, 4.rightLeft
        #Case 1 0r 3
        if( d > 1 and h == 1):

            # now we need to check if its a left or leftRight case
            # w is equal to -1,0,1 depending if root.right
            w = self.rightOrLeftHeavy(root.right)

            # if w = 0 or -1 then just left heavy and leftrotate
            # if w = 1 then right heavy and need a rightRotate(root.right) then leftRotate
            if(w == 1 or w == -1):
                root = self.left_Rotation(root)
            elif(w == 0):
                root.right = self.right_Rotation(root.right)
                root = self.left_Rotation(root)

        # Now we need to check for a right or rightLeft case
        if( d > 1 and h == 0):

            # now we nned to right or left case
            # w is equal to -1 0 1 depending if root.right
            w = self.rightOrLeftHeavy(root.left)

            # if w = 1 then just right heavy and right_rotate
            # if w = 0 or -1 then left heavy and left rotate(root.right) then right rotate
            if(w == -1 or w == 0):
                root = self.right_Rotation(root)
            elif(w == 1):
                root.left = self.left_Rotation(root.left)
                root = self.right_Rotation

    # This takes a val inserts it then as it ascedes to top it rotates to keep balance
    def insert(self, val):
        if(self.tree== None):
            self.tree= AVL_Node(val)
        else:
            self.wInsert(self.tree, val)

    # prints Tree using inOrder traversal
    def printTree(self,node):
        if( node != None):
            self.printTree(node.left)
            print(node.val)
            self.printTree(node.right)




def main():
    x = AVL_BST()
    x.insert(20)
    x.insert(4)
    x.insert(3)
    x.insert(1)
    x.insert(2)
    x.insert(29)
    x.insert(41)
    x.insert(50)
    x.printTree(x.getTree())

main()







