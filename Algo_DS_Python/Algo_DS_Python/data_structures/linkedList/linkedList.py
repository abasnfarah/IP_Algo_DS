"""
    Author: Abas Farah

    This is code for the linkedList class. And the Node class:

    The Properties of the Node Class:
        Atributes: data (int, str, list, tuple, etc) , next (Node)
        Methods: None

    The properties of the linkedList class are:
        Atributes: head (Node), size (int)
        Methods: insert, delete, printList, reverseIterative, reverseRecursive, recursivePrint, recursivePrintReverse 

"""

import copy

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, data=None):
        self.head = None if data is None else Node(data)
        self.size= 0 if data is None else 1
        # Added tail to make queue data structure implementation using linked list O(1) dequeue
        self.tail = None if data is None else self.head


    def __str__(self):
        ptr = self.head
        returnString = ''
        for i in range(0, self.size):
            returnString += " " + str(ptr.data)
            ptr = ptr.next

        if(self.size == 0):
            returnString = 'None'

        return returnString
    # This insert method has O(n) complexity becuase in the worst-case
    # it has to traverse every element in the list.
    # We will assume if no index is provided to insert at the very end of the list
    def insert(self, data, index=None):
        count = 0
        if (index == None and self.head != None):

            ptr = self.head
            tail = None

            # This loops to the very end of the list
            while ( ptr != None):
                tail = ptr
                ptr = ptr.next

            tail.next = Node(data)
            self.size += 1

            self.tail = tail.next

        elif( self.head == None):

            # if index doesn't equal zero and we have nothing in list then raise exception
            if (index != 0 and index != None):
                raise ValueError("Index out of bounds, No items in linkedList")

            else:
                self.head = Node(data)
                self.size = 1

                self.tail = self.head

        # Need to insert at head of item
        elif(index == 0):

            newNode = Node(data)
            newNode.next = copy.copy(self.head)
            self.head = newNode
            self.size += 1


        else:
            ptr = copy.copy(self.head)
            tail = None

            # This loops till count equals index unless indexIsOutBounds then just raises exception
            while(ptr != None and count < index):
                tail = ptr
                ptr = None if ptr.next == None else ptr.next
                count += 1

            # if ptr == None then it means that the index is longer then size of linkedList thus
            # raising exception
            if(ptr == None):
                raise ValueError("Index Out of bounds. linkedList is " + str(self.size) + " items Long")

            #if index is 0 just need to insert at head
            else:
                newNode = Node(data)
                tail.next = newNode
                newNode.next = ptr
                self.size += 1

    def insertTail(self, data):
        if( self.size == 0):
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
        else:
            newNode = Node(data)
            self.tail.next = newNode
            self.tail = self.tail.next
            self.size += 1

    def delete(self, index):

        # Exception handling if index is out of bounds
        if(index > self.size - 1):
            raise ValueError("Index Out of bounds. linkedList is " + str(self.size) + " items long")

        elif(index == 0):
            self.head = self.head.next
            self.size -= 1

        else:

            #iterate through list till item is found
            ptr = copy.copy(self.head)
            tail = None
            count = 0

            while(count < index):
                count += 1
                tail = ptr
                ptr = ptr.next

            if(tail != None):
                tail.next = ptr.next

            self.size -= 1
            if(self.size == 0):
                self.head = None

    def deleteItem(self, item):
        # Looping through list to find element then removing it from list
        # if our pointer is none will just exit function
        if(self.size != 0):
            if(self.size == 1 and self.head.data == item):
                self.head == None
                self.size -= 1
            ptr = self.head
            tail = None
            while(ptr != None and ptr.data != item):
                tail = ptr
                ptr = ptr.next

            if( ptr != None):
                tail.next = ptr.next
                self.size -= 1


    def getHead(self):

        if(self.size == 0):
            return None
        else:
            return self.head.data

    def getTail(self):

        if(self.size == 0):
            return None
        else:
            return self.tail.data


    def printList(self):
        if(self.head != None):

            ptr = self.head
            while(ptr != None):

                print(ptr.data)
                ptr = ptr.next

        else:

            print("LinkedList is Empty")

    # Calls recursive function to handle object atribute
    def recursivePrint(self): 
        self.wRecursivePrint(self.head)

    # Wrapper function for recursion    
    # this prints the linked list using recursion
    def wRecursivePrint(self, node):
        if(node != None):
            print(node.data)
            self.wRecursivePrint(node.next)

    def recursivePrintReverse(self):
        self.wRecursivePrintReverse(self.head)

    # Wrapper function for recursion
    # this prints the linked list in reverse order using recursion
    def wRecursivePrintReverse(self, node):
        if(node != None):
            self.wRecursivePrintReverse(node.next)
            print(node.data)

    # This reverses the linked list iteratively
    def reverseIterative(self):
        current = self.head
        prev = None
        nextPtr = None if current is None else current

        while(current != None):
            nextPtr = current.next
            current.next = prev
            prev = current
            current = nextPtr

        self.head = prev


    # This reverses the linked list recursively
    def reverseRecursive(self):
        self.wReverseRecursive(self.head)


    def wReverseRecursive(self,p):

        # Edge Case handleling
        if( self.head == None):
            print("This list is empty")
        elif( self.size == 1):
            print("This list only has one item")
        # Base Case
        elif(p.next == None):
            self.head = p
        else:
            self.wReverseRecursive(p.next)
            q = p.next
            p.next = None
            q.next = p


    def find(self,item):
        if(self.size == 0):
            return False
        elif(self.size == 1):

            value = True if self.head.data == item else False
            return value

        else:

            # Iterate through list till element is found
            ptr = self.head
            while(ptr != None and ptr.data == item):
                ptr = ptr.next

            # if element is found then ptr is not None
            if(ptr != None):
                return True

            return False






