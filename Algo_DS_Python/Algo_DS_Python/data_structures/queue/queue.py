"""
    Author: Abas Farah

    This is code for the arrayQueue class. And the listQueue class:

    The Properties of the arrayStack Class:
        Atributes: queue, front, back, size.
        Methods: enqueue, dequeue, peek, resize,

    The properties of the listStack class:
        Atributes: queue, front, back, size
        Methods: enqueue, dequeue, peek

"""

# Using linkedList python implementation
from Algo_DS_Python.data_structures.linkedList.linkedList import LinkedList

# Class definition for arrayQueue
# We are using the logical view that our queue is in a circular array.
class ArrayQueue:

    def __init__(self, data=None):
        self.queue = [None] * 10 if data is None else [data] + [None] * 9
        self.size = 1 if data is not None else 0
        self.front = 0 if data is not None else -1
        self.back = 0 if data is not None else -1

    def isEmpty(self):
        if (self.size == 0):
            return True
        else:
            return False

    # This adds to the circular array and if queue is full doesn't add to queue
    def enqueue(self, data):

        if ((self.back + 1)%len(self.queue) != self.front):
            if(self.size == 0):
                self.front = 0
                self.back = 0
            else:
                self.back = (self.back + 1) % len(self.queue)
            self.queue[self.back] = data
            self.size += 1
        else:
            print("Queue is Full")

    # This removes an element from the front of the queue
    def dequeue(self):
        if(self.size != 0):
            # if there is one element then front and back will be equal
            if(self.front == self.back):
                element = self.queue[self.front]
                self.front = -1
                self.back = -1
                return element
            else:
                element = self.queue[self.front]
                self.front = (self.front + 1) % len(self.queue)
                return element

class ListQueue:

    def __init__(self, data=None):
        self.queue = LinkedList(data)
        self.size = self.queue.size

    def isEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False

    def enqueue(self, data):
        self.queue.insertTail(data)
        self.size += 1

    # If queue is empty returns None 
    def dequeue(self):
        if (self.isEmpty()):
            return None
        element = self.queue.getHead()
        self.queue.delete(0)
        self.size -= 1
        return element


x = ListQueue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)

print(x.dequeue())
print(x.dequeue())
print(x.dequeue())







