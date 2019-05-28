// Merge Sort in C++
//
#include <iostream>
#include <stdio.h>

using namespace std;

void print_array(int arr[], int n)
{     
    int i;
    for(i = 0; i < n; i++){

        cout << arr[i] << " | " ;

    }

    cout << " <-- that was the array " << endl;
}



void print_array(int arr[], int l, int n)
{     
    for(int i = l; i < n; i++){

        cout << arr[i] << " | " ;

    }

    cout << " <-- that was the array " << endl;
}



void merge(int arr[], int l, int m, int m2, int n)
{
    //Create Copy arrays and values to work with
    int l1 = 0, l2 = 0, n1 = m-l, n2 = n - m2;
    int count = l;
    int len1 = (n1 - l1)+1;
    int len2 = (n2 - l2)+1;
    int arr1 [len1];
    int arr2 [len2];

    // populating the copy arrays
    for(int i = 0; i < len1; i++)
    {
        arr1[i] = arr[i+l];
    }
    print_array(arr1, len1);

    for(int i = 0; i < len2; i++)
    {
        arr2[i] = arr[m2 + i];
    }

    while(((l1 <= n1) && (l2 <= n2)) && count <= n){

        if(arr1[l1] < arr2[l2])
        {
            arr[count] = arr1[l1];
            l1++;
        } else 
        {
            arr[count] = arr2[l2];
            l2++;
        }
        count++;
    }

    // If one array is empty just populate using the other array
    while((l1 <= n1) && count <= n)
    {
        arr[count] = arr1[l1];
        l1++;
        count++;
    }

    while((l2 <= n2) && count <= n)
    { 
        arr[count] = arr2[l2];
        l2++;
        count++;
    }
 
}


void wrapperMergeSort(int arr[], int l, int n)
{
    int m = l+(n-l)/2;
    
    if(n>l)
    {
       wrapperMergeSort(arr,l,m); 
       wrapperMergeSort(arr,m+1, n);
       merge(arr,l,m,m+1,n);
       //print_array(arr,l,n);
    }
}


void mergeSort(int arr[], int n)
{
    wrapperMergeSort(arr,0,n-1);
}
int main()
{
    int arr[] = {6,3,2,8,1,21,4,7};
    int len = sizeof(arr)/sizeof(arr[0]);
    cout << len << " this is the length of the array "<< endl;
    mergeSort(arr,len);
    print_array(arr,len);

}

