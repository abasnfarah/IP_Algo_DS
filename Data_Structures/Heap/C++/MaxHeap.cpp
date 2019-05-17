/* This is the MaxHeap Class implementation 
   This is based on the notes from CLRS Heap Data Structure 
   The heap invariant is that all parent nodes are larger then it's children */ 
#include "MaxHeap.h" // User defined header in the same directory
#include <iostream>
#include <vector>

// Constructors
MaxHeap::MaxHeap(int *heap, int size){
    int n = size;
    this->heap.reserve(2*n);

    for(int i = 0; i < n; i++){
        this->heap.push_back(heap[i]);
    }

    this->buildMaxHeap(this->heap);

    this->size = n;
}


MaxHeap::MaxHeap(std::vector<int> heap){
    this->heap = heap;
    this->buildMaxHeap(this->heap);
    this->size = heap.size();
}


// Getters
std::vector<int> MaxHeap::getHeap() const {
    return this->heap;
}

int MaxHeap::getSize() const {
    return this->size;
}

// Prints the Heap to Terrminal
void MaxHeap::printHeap(std::vector<int> heap) const{

    std::cout << "Your Heap ==> ";
    for(auto i = heap.cbegin(); i != heap.cend(); i++){
        std::cout << *i << " | ";
    }
    std::cout << "\n";

}    

// this holds the heap invariant by putting the int at heap[i] in place given subtrees are heaps
void MaxHeap::maxHeapify(std::vector<int> heap, int i){    
    int left = (i * 2) + 1;
    int right = i * 2;
    int largest = 0;

    if (left < this->size && heap[left] > heap[i]){
        largest = left;
    } else {
        largest = i;
    }

    if (right < this->size && heap[right] > heap[largest]){
        largest = right;
    }
    
    if (largest != i){
        int temp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = temp;
        this->maxHeapify(heap, largest);
    }
}

// This builds a heap by working our way from the leaf nodes and up maintaining the heap invaiant
void MaxHeap::buildMaxHeap(std::vector<int> heap){
    for( int i = this->size/2; i >= 0; i--){ 
        this->maxHeapify(heap, i);
    }
}

int MaxHeap::extractMax(){
    int m;
    if ( this->size > 1 ){
        m = this->heap[0];
        this->heap[0] = this->heap[this->size-1];
        this->heap[this->size-1] = m;
        this->size--;
        this->maxHeapify(this->heap, 0);
        return m;
    } else if(this->size == 1) {
        this->size--;
        return this->heap[0];
    } else{
        throw "The Heap is Empty can't extract max";
    }
}

// This returns the index of a parent given a nodes index
int MaxHeap::getParent(int i){
    int parent = 0;

    if (i == 0){ // root node
        std::cout << "Item is a root node" << std::endl;
        return i;

    }else if( i % 2 == 0){ // Even
        parent = (i/2) - 1;
    } else {               // Odd
        parent = i/2;
    }
    return parent;


}

void MaxHeap::siftUp(std::vector<int> heap, int i){
    // Need to find parent
    // if odd number then /2 if even /2 -1
    int parent = this->getParent(i);
    if(i == 0){
        std::cout << "Item is at root node. Can't sift up further" << std::endl;
    } else {
        int temp = heap[i];
        heap[i] = heap[parent];
        heap[parent] = temp;
    }

}

void MaxHeap::insert(int x){

    // Add element to end of array
    this->heap.push_back(x);
    this->size++; 

    int parent = this->getParent(this->size-1);
    int child = this->size - 1;

    while( child != 0 && this->heap[child] > this->heap[parent]){

        this->siftUp(this->heap, child);
        child = parent;
        parent = this->getParent(child);

    }
}

void MaxHeap::heapSort(int *heap, int size){
    MaxHeap a(heap, size);
    std::vector<int> A;
    for(int i = 0; i < size; i++){
        a.extractMax();
    }

    A = a.getHeap();
    // Copy vector into array
    for(int i = 0; i < size; i++){
        heap[i] = A[i];
    } 
}

void MaxHeap::heapSort(std::vector<int> heap){
    MaxHeap a(heap);

    for(int i = 0; i < heap.size(); i++){
        a.extractMax();
    }
    
    heap = a.getHeap();
}






