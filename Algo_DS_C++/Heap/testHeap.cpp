/* A test driver for the MaxHeap class (testHeap.cpp */
#include <iostream>
#include "MaxHeap.h"
typedef std::vector<int> int_vec;

using namespace std;

void printArr(int arr[], int size){
    for(int i = 0; i < size; i++){
        cout << arr[i] << " | ";
    }
        cout << endl;
}

void printVec(int_vec vec){
    for(int i = 0; i < vec.size(); i++){
        cout << vec[i] << " | ";
    }
}

int main() {
    int_vec arr = {6,3,2,8,1,21,4,7};
    MaxHeap h(arr);
    h.heapSort(arr);
    printVec(arr);

    return 0;
}
