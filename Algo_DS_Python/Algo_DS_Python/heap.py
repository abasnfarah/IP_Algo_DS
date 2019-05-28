import operator
import math

class MaxHeap: 
    # Class for max Heap. 
    # Methods:
    # max_heapify, build_max_heap, insert, extract_max, heapSort 
    
    def __init__(self, heap=None):
        self.__heap = [] if heap is None else self.build_max_heap(heap)
        self.__size = 0 if heap is None else len(heap) 
        self.__height = 0 if heap is None else len(heap).bit_length()

    def __str__(self):
        return str(self.__heap)

    # Getters 
    def getHeap(self):
        return self.__heap
    
    def getSize(self):
        return self.__size
    
    def getHeight(self):
        return self.__height

#    def setHeap(heap):
#        self.__heap = [] if heap is None else build_max_heap(heap)
#        self.__size = 0 if heap is None else len(heap) 
#        self.__height = 0 if heap is None else len(heap).bit_length()
    
    def max_heapify(self,h,i):
        left = (i * 2) + 1
        right = i * 2 
        largest = 0

        if(left < len(h) and h[left] > h[i]):
            largest = left
        else:
            largest = i
    
        if(right < len(h) and h[right] > h[largest]):
            largest = right

        if(largest != i):
            temp = h[i]
            h[i] = h[largest]
            h[largest] = temp
            self.max_heapify(h,largest) 

    def build_max_heap(self,h): 
        for i in range((len(h)//2), -1, -1):
            self.max_heapify(h,i)

        return h

    def insert(self,i):
        # first swap the max element with i then build max heap 
        h = self.__heap;
        h.append(i)
        self.__heap = self.build_max_heap(h)

    def extract_max(self):
        return h[0] if h != None else None
    
    # this is gonna be a static method so it can run on any array
    @staticmethod
    def heapSort(arr):
        # creates heap from array 
        a = MaxHeap(arr).getHeap()
        h = []
        for i in range(0,len(a)):
            h = [a[0]] + h
            a = MaxHeap(a[1:]).getHeap()

        return h

        


class MinHeap:
    # Class for max Heap. 
    # Methods:
    # min_heapify, build_min_Heap, insert, extract_min, heapSort 
    
    def __init__(self, heap=None):
        self.__heap = [] if heap is None else self.build_min_heap(heap)
        self.__size = 0 if heap is None else len(heap) 
        self.__height = 0 if heap is None else len(heap).bit_length()

    def __str__(self):
        return str(self.__heap)

    # Getters 
    def getHeap(self):
        return self.__heap
    
    def getSize(self):
        return self.__size
    
    def getHeight(self):
        return self.__height

#    def setHeap(heap):
#        self.__heap = [] if heap is None else build_min_heap(heap)
#        self.__size = 0 if heap is None else len(heap) 
#        self.__height = 0 if heap is None else len(heap).bit_length()
    
    def min_heapify(self,h,i):
        left = (i * 2) + 1
        right = i * 2 
        smallest = 0

        if(left < len(h) and h[left] <  h[i]):
            smallest = left
        else:
            smallest = i
    
        if(right < len(h) and h[right] <  h[smallest]):
            smallest = right

        if(smallest!= i):
            temp = h[i]
            h[i] = h[smallest]
            h[smallest] = temp
            self.min_heapify(h,smallest) 

    def build_min_heap(self,h): 
        for i in range((len(h)//2), -1, -1):
            self.min_heapify(h,i)

        return h

    def insert(self,i):
        # first swap the min element with i then build min heap 
        h = self.__heap;
        h.append(i)
        self.__heap = self.build_min_heap(h)

    # this is gonna be a static method so it can run on any array
    @staticmethod
    def heapSort(arr):
        # creates heap from array 
        a = MinHeap(arr).getHeap()
        h = []
        for i in range(0,len(a)):
            h = h + [a[0]] 
            a = MinHeap(a[1:]).getHeap()

        return h


def main():
    heap = MinHeap([2,3,4,1,5,9,8,15])
    print(heap)
    heap.insert(6)
    print(heap)
    arr = heap.getHeap()
    print(heap.heapSort(arr))


def left(x):
    return x * 2

def right(x):
    return (x *2) + 1

def max_Heapify(arr,largest): 
    l = left(largest)

main()
