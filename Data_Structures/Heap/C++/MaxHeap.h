// This is the header file for the MaxHeap Class

#ifndef MAXHEAP_H
#define MAXHEAP_H
#include <vector>

class MaxHeap {
    private:
        std::vector<int> heap;
        int size;
    public:
        // constructor prototype
        MaxHeap(int *heap,int size);
        MaxHeap(std::vector<int> heap);

        //getter Prototypes
        std::vector<int>  getHeap() const;
        int getSize() const;

        //Heap Methods
        void printHeap(std::vector<int> heap) const;
        void maxHeapify(std::vector<int> heap, int i);
        void buildMaxHeap(std::vector<int> heap);
        int extractMax(); 
        int getParent(int i);
        void siftUp(std::vector<int> heap, int i);
        void insert(int x);
        static void heapSort(int *heap, int size);
        static void heapSort(std::vector<int> heap);
};

#endif
