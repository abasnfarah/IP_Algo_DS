"""
    Author: Abas Farah

    This is the function definition for RadixSort.

    RadixSort sorts a limited imput by using a stable sub-routine
    sorting algorithm. It runs through the array d times where d is
    the largest digit number  D < {1,10,100,1000,...,}.

    It then runs through the and sorts based on the last digit to
    the first digit. for example:
    [1, 32, 54, 28, 320, 597] --> [320, 1, 32, 54, 597, 28] on the first pass
    [1, 28, 320, 54, 597] --> on the second pass
    [1, 28, 54, 320, 597] --> on the last pass.
    D in this case is 3 becuase the largest digit place is 100th.

    The time complexity of this sorting algorith is
    O(d*(n+b)) where d is the length of the digit place and n is how long
    it takes because of counting Sort sub routine runs O(n + K) where k is
    the largest number. k = B is the base number.
    in this case B would be 10 becuase the numbers are base 10.

    Implemented using psuedocode from ClRS Textbook

"""

# This is counting sort just modified to take in what digit place we 
# are sorting from
def countingRadixSort(A, k, d):

    # Creating a new array
    c = [None] * (k)

    # Populates our counter array to all zeros
    for i in range(0, k):
        #print(i)
        c[i] = 0

    # Then it starts counting our elements
    # This looks at -d str place so if d == 2 and s = [034]
    # then s[-d] = 3
    for j in range(0, len(A)):
        c[ int( A[j][-d] ) ] = c[int( A[j][-d] )] + 1

    # This then updates C to have all elements
    # Less then or equal to i
    for i in range(1, k):
        c[i] = c[i] + c[i-1]

    B = [None] * (len(A))

    for j in range(len(A) - 1, -1, -1):
        #print(j)
        B[c[int(A[j][-d])] - 1] = A[j]
        c[int( A[j][-d]) ] = c[int( A[j][-d])] - 1

    return B


def radix_Sort(A, d):

    # Creating an array that has digits equal and filled with zero
    # as needed, EX: [1, 49, 4, 348, 9, 10] --> [001, 049, 004, 348, 009, 010]
    B = []
    for i in A:
        B.append(str(i).zfill(d))

    # Now sort based on digits
    for i in range(1, d + 1):
        B = countingRadixSort(B, 10, i)

    for i in range(0, len(B)):
        A[i] = int(B[i])


