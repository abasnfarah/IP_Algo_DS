"""
    Author: Abas Farah

    This is code for the arrayStack class. And the listStack class:

    The Properties of the arrayStack Class:
        Atributes: stack, top, size.
        Methods: push, pop, peek, resize,

    The properties of the listStack class:
        Atributes: stack, size
        Methods: push, pop, peek

    Functions utilizing the Stack data Structure:
        reverseString()
        checkForBalancedParentheses()
        infixToPrefix()
        infixToPostfix()
        prefix()
        postfix()

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
            strStack.push(i)
        # Once a closing paren is given we need to check if it is balanced
        # if our input matches then we keep going or return false
        elif(i == ')' or i =='}' or i == ']'):
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

# This function takes two operands x and s and returns true if s has lower precedence then x
def lowerPrecedence(x, s):
    if ((x == '*' and s == '+') or (x == '*' and s == '-')):
        return True
    elif ((x == '/' and s == '+') or (x == '/' and s == '-')): 
        return True
    else :
        return False


# This method takes a infix expression: (1 + 2) * 5 --> 1 2 5 + *
# The order of operants never change A + b * C --> A B C + * 
def infixToPostfix(s):

    strStack = ArrayStack()
    postfix = ''

    # Check if infix has balanced paren
    if(checkBalancedParentheses(s) == False):
        print("infix expression not balanced")
        return s

    for x in s:

        if (x == '*' or x == '+' or x == '-' or x == '/' or x == '(' or x == ')'):
            # need to check if stack is empty
            if(strStack.isEmpty()):
                strStack.push(x)

            # If whats on the stack has lower precedence then we can just push
            elif( lowerPrecedence(x, strStack.peek()) ):
                strStack.push(x)

            # Now x is either above a opening paren or lowerPrecedence
            elif( strStack.peek() == '('):
                strStack.push(x)

            elif( x == '(' ):
                strStack.push(x)

            # Since we hit a closing paren we need to pop and write all operators
            elif( x == ')'):
                operatorString = ''
                # now we need to traverse the stack till we hit a closing paren
                while((strStack.isEmpty() == False) and strStack.peek() != '('):
                    operatorString += strStack.pop()

                # After the loop we hit a opening bracket and need to pop once more to get rid of it
                postfix += operatorString
                strStack.pop()

            # now we know that x is lowerPrecedence then whats on the stack 
            # not surrounded by a paren. in this case we pop the stack till 
            # it's empty or we hit a opening paren and write to our return string
            else:
                while((strStack.isEmpty() == False) and strStack.peek() != '('):
                    postfix += strStack.pop()

                strStack.push(x)


        # if x doesn't equal a space, operator  or paren then we can just push
        elif( x != ' '):
            postfix += x

    # now we want to push whats left in the stack to the return string
    while(strStack.isEmpty() == False):
        postfix += strStack.pop()
    return postfix

# This method takes a infix expression: (1 + 2) * 5 --> *+125
# The order of operants never change A + b * C --> *+ABC

def infixToPrefix(s):

    strStack = ArrayStack()
    prefix = ''

    # Check if infix has balanced paren
    if(checkBalancedParentheses(s) == False):
        print("infix expression not balanced")
        return s

    for x in s:

        if (x == '*' or x == '+' or x == '-' or x == '/' or x == '(' or x == ')'):
            # need to check if stack is empty
            if(strStack.isEmpty()):
                strStack.push(x)

            # If whats on the stack has lower precedence then we can just push
            elif( lowerPrecedence(x, strStack.peek()) ):
                strStack.push(x)

            # Now x is either above a opening paren or lowerPrecedence
            elif( strStack.peek() == '('):
                strStack.push(x)

            elif( x == '(' ):
                strStack.push(x)

            # Since we hit a closing paren we need to pop and write all operators
            elif( x == ')'):
                operatorString = ''
                # now we need to traverse the stack till we hit a closing paren
                while((strStack.isEmpty() == False) and strStack.peek() != '('):
                    operatorString = strStack.pop() + operatorString

                # After the loop we hit a opening bracket and need to pop once more to get rid of it
                prefix = operatorString + prefix
                strStack.pop()

            # now we know that x is lowerPrecedence then whats on the stack 
            # not surrounded by a paren. in this case we pop the stack till 
            # it's empty or we hit a opening paren and write to our return string
            else:
                while((strStack.isEmpty() == False) and strStack.peek() != '('):
                    prefix = strStack.pop() + prefix

                strStack.push(x)


        # if x doesn't equal a space, operator  or paren then we can just push
        elif( x != ' '):
            prefix += x

    # now we want to push whats left in the stack to the return string
    while(strStack.isEmpty() == False):
        prefix = strStack.pop() + prefix
    return prefix



# This evaluates a prefix expression x and returns an integer value
# Assume that the string passed is a valid postfix expression
def postfix(s):

    # create a stack to hold operants
    operantStack = ListStack()
    value = 0

    # Now we will go through the string and evaulate the expression
    for x in s:
        # we'll check for operant
        if (x == '*' or x == '/' or x == '-' or x == '+'):
            # now we need to pop last two values
            A = operantStack.pop()
            B = operantStack.pop()

            if(x == '*'):
                value = B * A
                operantStack.push(value)
            elif(x == '/'):
                value = B / A
                operantStack.push(value)
            elif(x == '-'):
                value = B - A
                operantStack.push(value)
            elif(x == '+'):
                value = B + A
                operantStack.push(value)
        elif (x != ' '):
           y = int(x) 
           operantStack.push(y)

    return operantStack.pop()


# This function evaluates a prefix expression and returns a integer value
# Assume that the string passed is a valid postfix expression
def prefix(s):
    # Create a stack to hold operants
    operantStack = ArrayStack()
    value = 0

    # Now we will go through the string and evaluate the expression
    for x in reversed(s):
        # We will check for operant
        if (x == '*' or x == '/' or x == '-' or x == '+'):

            B = operantStack.pop()
            A = operantStack.pop()

            if(x == '*'):
                value = B * A
                operantStack.push(value)
            elif(x == '/'):
                value = B / A
                operantStack.push(value)
            elif(x == '-'):
                value = B - A
                operantStack.push(value)
            elif(x == '+'):
                value = B + A
                operantStack.push(value)
        elif (x != ' '):
           y = int(x) 
           operantStack.push(y)

    return operantStack.pop()

























































