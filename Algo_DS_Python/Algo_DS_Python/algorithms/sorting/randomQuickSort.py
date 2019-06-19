"""
  Author: Abas Farah

  This is a Python file for the randomized quicksort ALgorithm. This uses the psuedocode from ClRS Textbook.

  The runtime of this algorithm is worstcase O(nlgn) time.
  The average runtime of this algorithm is theta O(nlgn)
  The reason for this is becuase it uses the same algorithm as quicksort just randomizing the partitioning
  thus enabiling on average a nlgn time complexity

  The way quickSOrt works is by using the divide and conquor paradigm to sort an array inplace. It
  does this by partitioning the array A[p ,, r] into two subarrays A[p..q-1] and A[q+1...r] such that
  every element of a[p..q-1] is less than or equal to a[q] and A[q+1..r].

  After partitioning you sort the two subarrays by recursive calls to quicksort.

"""
from quickSort import partition
import random

def randomized_Partition(A, p, r):
    i = random.randint(p,r)
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return partition(A, p, r)


def randomized_QuickSort(A, p, r):
    if p<r:
        q = randomized_Partition(A, p, r)
        randomized_QuickSort(A, p, q-1)
        randomized_QuickSort(A, p, r)





