

def insertionSort(arr):
    for i in range(1,len(arr)): 
        s = arr[i]
        j = i
        while( j > 0 and arr[j-1] > s): 
            arr[j] = arr[j-1]  
            j-= 1
        arr[j] = s

