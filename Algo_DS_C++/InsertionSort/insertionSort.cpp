// Insertion Sort: Binary and normal insertion sort

#include <iostream>
#include <stdio.h>

using namespace std;

// insertion sort given an array arr and the length of that array n
// O(n^2) running time
void insertionSort(int arr[], int n)
{
    int i, j, tmp; 
    for(i = 1; i < n; i++){
        j = i;
        while(j > 0 && arr[j - 1] > arr[j]){ 

            tmp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = tmp;
            j--;
            
        }
    }
}

// This searches for a value S, and returns the index for where it is 
// or where the value just smaller is.
int binarySearch(int arr[], int l, int n, int s)
{
    int m = (l+n)/2;
    
    if(l >= n) {
        if(arr[l] < s){
        return l+1;

        } else {
        return l;
        }
    }

    if(arr[m] >  s) {
        return binarySearch(arr, l, m - 1, s);
    } else {
        return binarySearch(arr, m + 1, n, s);
    }

}

void print_array(int arr[], int n)
{     
    int i;
    for(i = 0; i < n; i++){

        cout << arr[i] << " | " ;

    }

    cout << " <-- that was the array " << endl;
}


// doesn't quite work yet
void binaryInsertionSort(int arr[], int n)
{
    int i, j, temp, temp2;

    for(int i = 1; i < n; i++){        
//        cout << arr[i] << endl;
//        cout << i << endl;
        j = binarySearch(arr, 0, i-1, arr[i]);
        temp = arr[j];
        arr[j] = arr[i];
        while(j < i){
            j++; 
            temp2 = arr[j];
            arr[j] = temp; 
            temp = temp2;
//            cout << temp2 << endl;
        }
        print_array(arr, n);
    }


}

