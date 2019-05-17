// This is the code for the Heap data structure and all it's methods

#include <iostream>
#include <stdio.h>

using namespace std;

class MaxHeap
{
    // Class for Max Heap
    // Methods:
    // Max_heapify, build_max_heap, insert, extract_max, heapsort

    private:
        int *heap;
        int size;    

    public:
        MaxHeap(int arr[] = []): heap(buildMaxHeap(arr)), size(length(arr)) {
            intilize();
        }

        MaxHeap(int arr[])
        {    
            initilize(arr);
        }


        ~MaxHeap
}
