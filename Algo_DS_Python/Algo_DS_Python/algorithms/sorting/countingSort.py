"""
    Author: Abas Farah

    This is the function definition for countingSort.

    Counting Sort sorts an array of n keys if the keys are
    integers --> {0,1,..., k-1}

    Counting sort then places these items in order based of K
    The time complexity is O(n + K).

    if we can get k == n then it is O(n) time complexity.

    Implemented using psuedocode from ClRS Textbook

"""

def countingSort(A, k):

    # Creating a new array
    c = [None] * (k +1)

    # Populates our counter array to all zeros
    for i in range(0, k + 1):
        c[i] = 0

    # Then it starts counting our elements
    for j in range(0, len(A)):
        c[A[j]] = c[A[j]] + 1

    # This then updates C to have all elements
    # Less then or equal to i
    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]

    B = [None] * (len(A))

    for j in range(len(A) - 1, -1, -1):
        B[c[A[j]] - 1] = A[j]
        c[A[j]] = c[A[j]] - 1

    return B


