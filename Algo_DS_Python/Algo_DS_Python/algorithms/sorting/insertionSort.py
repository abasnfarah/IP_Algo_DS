

def insertionSort(arr):
    for i in range(1,len(arr)): 
        s = arr[i]
        j = i
        while( j > 0 and arr[j-1] > s): 
            arr[j] = arr[j-1]  
            j-= 1
        arr[j] = s

def main():
    x = [3,6,2,8,1,21,4,7]
    insertionSort(x)
    print(x)

main()
