"""
  Author: Abas Farah

  This is a Python file for the quicksort ALgorithm. This uses the psuedocode from ClRS Textbook.

  The runtime of this algorithm is worstcase O(n^2) time.
  The average runtime of this algorithm is theta O(nlgn)

  The way quickSOrt works is by using the divide and conquor paradigm to sort an array inplace. It
  does this by partitioning the array A[p ,, r] into two subarrays A[p..q-1] and A[q+1...r] such that
  every element of a[p..q-1] is less than or equal to a[q] and A[q+1..r].

  After partitioning you sort the two subarrays by recursive calls to quicksort.

"""
import copy

# Lets Begin with the important procedure of Partitioning the array
# This function rearanges the subarray A[p..r] in place
def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<=x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i + 1

def wQuickSort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        wQuickSort(A, p, q-1)
        wQuickSort(A, q+1, r)

def quickSort(A):
    wQuickSort(A,0, len(A)-1)

