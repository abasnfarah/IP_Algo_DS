"""
    Author: Abas Farah

    This is code for the arrayStack class. And the listStack class:

    The Properties of the arrayStack Class:
        Atributes: stack, top, size.
        Methods: push, pop, peek, resize,

    The properties of the listStack class:
        Atributes: stack, size
        Methods: push, pop, peek

"""

# Using linkedList python implementation 
from Algo_DS_Python.data_structures.linkedList.linkedList import LinkedList

# Class definition of arrayStack
class ArrayStack:

    # Initilizer Function
    def __init__(self, data=None):
        self.stack = [None] * 10 if data is None else [data] + [None] * 9
        self.size = 1 if data is not None else 0
        self.top = 0 if data is not None else -1

    def isEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False

    # resize Method. This resizes the array to 2*len(Array) when array size is exhausted
    # Complexity O(2n), linear
    def resize(self):
        newArr = [None] * (len(self.stack)*2)

        for i in range(0, len(self.stack)):
            newArr[i] = self.stack[i]

        self.stack = newArr

    # push method this pushes elements on to the array and resizes it if array size is reached
    # Best case O(1), worst case O(n) due to resizing, Average case O(1).
    def push(self, data):
        # This checks if we need to resize the array
        if (self.size + 1 == len(self.stack)):
            self.resize()

        # Otherwise we can just add to the stack
        self.top += 1
        self.stack[self.top] = data
        self.size += 1

    # This returns the top element and decrements our stack by 1
    # Complexity is O(1), constant
    def pop(self):

        if(self.size == 0):
            print("Stack is Empty. ")
            return None
        else:
            element = self.stack[self.top]
            self.top -= 1
            self.size -= 1
            return element

    # This returns the element at the top without poping it out of stack
    # Complexity is O(1), constant
    def peek(self):

        if(self.size == 0):
            print("Stack is Empty. ")
            return None
        else:
            element = self.stack[self.top]
            return element

    # This is function for testing in terminal
    def printStack(self):
        for i in range(0, self.size):
            print(self.stack[i])

class ListStack:

    def __init__(self, data=None):
        self.stack = LinkedList(data)
        self.size = self.stack.size

    def isEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False

    # This takes O(1) time since inserting at head of linkedList
    def push(self, data):
        self.stack.insert(data,0)
        self.size += 1

    # This takes O(1) time since deleting from head of linkedlist
    # If stack is empty will raise ValueError
    def pop(self):
        element = self.stack.getHead()
        self.stack.delete(0)
        self.size -= 1
        return element

    def peek(self):
        return self.stack.getHead()

    def getList(self):
        return self.stack

# O(n) time
def reverseString(x):
    s = ArrayStack();

    for i in x:
        s.push(i)

    w = ""

    for i in range(0, len(x)):
        w += s.pop()

    return w

# O(N) time
# This function checks if a given string has balanced paren (), {}, []. return boolean
def checkBalancedParentheses(inputString):

    strStack = ListStack()
    # Looping through string
    for i in inputString:
        # if we have a opening paren then push to stack
        if(i == '(' or i == '{' or i == '[' ):
            print(i)
            strStack.push(i)
        # Once a closing paren is given we need to check if it is balanced
        # if our input matches then we keep going or return false
        elif(i == ')' or i =='}' or i == ']'):
            print(i)
            if(strStack.isEmpty()):
                return False
            x = strStack.pop()
            if(i == ')' and x != '('):
                return False
            if(i == ']' and x != '['):
                return False
            if(i == '}' and x != '{'):
                return False

    if(strStack.isEmpty()):
        return True
    else:
        return False




