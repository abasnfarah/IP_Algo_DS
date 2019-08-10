"""
    Author: Abas Farah

    This is code for fib (fibonacci number):
        it takes an imput n and returns the nth fibonacci number

    1. There is going to be the naive fib function that uses recursion
    2. Second function uses memoization to optimize the solution
    3. The second function does this but using the bottom up dynamic programming method

"""


# This is the naive solution
# The runtime for this algorithm is O(2^n) (really really bad!!!)
def fib(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fib(n-1) + fib(n-2)

# Basic memoized algorithm for fib 
# The runtime for this algorithm is O(n) but also uses O(N) space (A lot faster!!!)
def fibMemo(n,memo={1:1,0:0}):
    if(n in memo):
        return memo[n]
    else:
        f = fibMemo(n-1,memo) + fibMemo(n-2,memo)
        memo[n] = f
        return f

# This is the DP implementation but instead of doing it top-down like the last function
# we would be building our memo Set through bottom up strategy
# The runtime for this algorithm is O(n) and uses O(n) space too, however saves us the 
# costly recursion
def fibMemoBottomUp(n):
    # creating fib hashTable for building up
    f = 0
    fib = {}
    for k in range(1, n+1):
        if(k <= 2):
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]

# This is the same as the last function but just keeping track of the last two parts of 
# of the equation saving some extra space
# The runtime for this algorithm si O(n) and only uses O(1) space
def fibMemoBottomUpOptimized(n):
    # this is the same as the las
    f1 = 0
    f2 = 0

    for k in range(1, n+1):
        if(k == 1):
            f1 = 1
        else:
            temp = f1
            f1 = f1 + f2
            f2 = temp
    return f1

if __name__=="__main__":
    print(fibMemo(10))


















