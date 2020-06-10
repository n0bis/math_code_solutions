import random
import time
import math

# Provide a uniform interface to the sorting algorithm like all of the other sorting algorithms.
# To make the comparisons fair, we don't give counting sort the largest integer in its input; it
# has to find that on its own. The reasoning is that why would we give counting sort some extra information
# it uses in its sorting when 1) it can find that information on its own, and 2) the other sorting algorithms
# we have implemented are not given extra information that could be helpful to them.

# Extra note: we use max to find the max integer in input. One could argue that this is not fair, as max
# is built-in and implemented in C (https://github.com/python/cpython/blob/master/Python/bltinmodule.c#L1584)
# and we should instead re-implement the max function in Python to make the comparison fair.. lets just stick with max.
def counting_sort(A):
    # We give A.copy() as the first argument and A as the second, as this will have the effect that
    # counting_sort_internal will write the sorted numbers in A, which is what the users of our function expects.
    counting_sort_internal(A.copy(), A, max(A) if len(A) > 0 else 0)

def counting_sort_internal(A, B, k):
    C = [0] * (k+1)

    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]

    for j in reversed(range(len(A))):
        # NOTE: we have to subtract 1 when indexing into B, as in the pseudocode, B is 1-indexed.
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1
    
    print(f'C: {C}')

##########################################

def quick_sort(A):
    quick_sort_internal(A, 0, len(A) - 1)

def quick_sort_internal(A, p, r):
    if p < r:
        q = partition(A,p,r)
        quick_sort_internal(A, p, q-1)
        quick_sort_internal(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            exchange(A,i,j)

    exchange(A,i+1,r)
    return i + 1

def exchange(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

##########################################

def quick_sort_optimized(A):
    quick_sort_optimized_internal(A, 0, len(A) - 1)

def quick_sort_optimized_internal(A, p, r):
    size = r-p+1

    if size >= 16:
        q = partition_optimized(A,p,r)
        quick_sort_optimized_internal(A, p, q-1)
        quick_sort_optimized_internal(A, q+1, r)
    elif size >= 1:
        q = partition(A,p,r)
        quick_sort_internal(A, p, q-1)
        quick_sort_internal(A, q+1, r)

# Uses the median of the first, middle and last element of the array
# as pivot. Does this by simply swapping this element with the
# last element that we would usually pick as the pivot, and then
# calls the standard partition function.
# Not at all optimized to use as few comparisons as possible
# (actually kind of a dumb implementation; could be done faster).
def partition_optimized(A, p, r):
    first = A[p]
    middle = A[int((p+r)/2)]
    last = A[r]

    if middle <= first <= last or last <= first <= middle:
        # first is median
        exchange(A,p,r)
    elif first <= middle <= last or last <= middle <= first:
        # middle is median
        exchange(A,int((p+r)/2),r)
    else:
        # last is median (meaning it is already in the correct spot)
        pass

    return partition(A,p,r)

##########################################

def merge_sort(A):
    # initially, sort the entire array
    # important: remember that the array goes from 0 to length - 1
    # (r should be equal to the last index initially)
    merge_sort_internal(A, 0, len(A) - 1)

def merge_sort_internal(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort_internal(A, p, q)
        merge_sort_internal(A, q+1, r)
        merge(A, p, q, r)

# We use 0-indexing, while CLRS uses 1-indexing.
def merge(A, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q

    L = [0] * (n_1 + 1)
    R = [0] * (n_2 + 1)

    for i in range(n_1):
        L[i] = A[p+i]

    for j in range(n_2):
        R[j] = A[q+1+j]

    L[n_1] = math.inf
    R[n_2] = math.inf

    i = 0
    j = 0

    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

##########################################

def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

##########################################

def test():
    print("Random list")
    A = list(range(10))
    random.shuffle(A)
    print(A)
    counting_sort(A) 
    print(A)
    print()

    print("Duplicates")
    A = [6,8,4,3,4,7,4,3,21,2,4,56,3,3,3,3,1,2,3,4,5]
    print(A)
    counting_sort(A) 
    print(A)
    print()

    print("Already sorted list")
    A = list(range(10))
    print(A)
    counting_sort(A) 
    print(A)
    print()

    print("Reverse sorted list")
    A = list(range(10))
    A = list(reversed(A))
    print(A)
    counting_sort(A) 
    print(A)
    print()

    print("List with 1 element")
    A = [42]
    print(A)
    counting_sort(A) 
    print(A)
    print()

    print("Empty list")
    A = []
    print(A)
    counting_sort(A) 
    print(A)
    print()

def timing_random(n):
    tries = 3
    total_execution_time = 0

    ks = [int(n/50), n, 50*n]

    for k in ks:
        for i in range(tries):
            A = [random.randint(0,k) for _ in range(n)]

            start_time = time.time()
            counting_sort(A)
            end_time = time.time()

            execution_time = end_time - start_time

            total_execution_time += execution_time

        average_time = total_execution_time / tries

        print("Size:", n, " k:", k)
        print("Average time:", average_time)
        print("average_time / (n + k):", average_time / (n + k))
        print()

# NOTE: the comparison to the built-in python sorting is not "fair":
# the built-in sorting is implemented in C (https://github.com/python/cpython/blob/v3.8.1/Objects/listobject.c#L2212)
# meaning that it runs without having to be interpreted by the python interpreter.
# Even if we were to implement the exact same algorithm in python, it would not run as fast as the built-in.
def sorting_comparison(n, k):
    print("Size:", n)
    print()

    tries = 3

    sorting_functions = [("Counting sort", counting_sort), ("Mergesort", merge_sort), ("Quicksort", quick_sort),
                         ("Quicksort (optimized)", quick_sort_optimized), ("Sort (python)", list.sort)]

    A = [random.randint(0,k) for _ in range(n)]

    for name,function in sorting_functions:
        total_execution_time = 0
        
        for i in range(tries):
            B = A.copy()

            start_time = time.time()
            function(B)
            end_time = time.time()

            execution_time = end_time - start_time

            total_execution_time += execution_time

        average_time = total_execution_time / tries

        print("Function:", name)
        print("Average time:", average_time)
        print()

if __name__ == "__main__":
    A = [3, 1, 4, 3, 5, 0, 3, 1]

    #merge_sort(A)

    #counting_sort(A)

    #quick_sort(A)

    #quick_sort_optimized(A)

    counting_sort_internal(A.copy(), A, 6)

    #insertionSort(A)

    print(f'result: {A}')

    # TEST HOW FAST IT IS / WHETHER OUR TIME COMPLEXITY ANALYSIS IS CORRECT
    # timing_random(40000)
    # print("-"*50)
    # timing_random(80000)
    # print("-"*50)
    # timing_random(120000)

    # COMPARE SORTING ALGORITHMS FOR DIFFERENT K
    # n = 50000
    # print("k = n/50")
    # sorting_comparison(n, int(n/50))
    # print("-"*50)
    # print("k = n")
    # sorting_comparison(n, n)
    # print("-"*50)
    # print("k = 50*n")
    # sorting_comparison(n, 50*n)