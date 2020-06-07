from math import floor


def minHeapify(A, i):
    """
       Maintaining the min-heap property

       :param list A: The priority queue
       :param int i: The current index
    """
    l = left(i)
    r = right(i)
    if l <= len(A) - 1 and A[l] < A[i]:
        lowest = l
    else:
        lowest = i
    if r <= len(A) - 1 and A[r] < A[lowest]:
        lowest = r
    if lowest != i:
        A[i], A[lowest] = A[lowest], A[i]
        minHeapify(A, lowest)

def maxHeapify(A, i):
    n = len(A) - 1
    l = left(i)
    r = right(i)
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)

def buildMaxHeap(A):
    n = len(A) - 1
    for i in range(n//2, -1, -1):
        maxHeapify(A, i)

def buildMinHeap(A):
    n = len(A) - 1
    for i in range(n//2, -1, -1):
        minHeapify(A, i)

def extractMin(A):
    """
       Extracting the minimum value from the priority queue

       :param list A: The priority queue
       :return int min: The minimum value
    """
    min = A[0]
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    A.pop()

    minHeapify(A, 0)
    return min

def extractMax(A):
    max = A[0]
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    A.pop()

    maxHeapify(A, 0)
    return max

def insert(A, key):
    """
       Inserts a new value onto the priority queue

       :param list A: The priority queue
       :param int key: The value to be inserted into the priority queue
    """
    A.append(key)
    i = len(A) - 1
    while i >= 0 and A[parent(i)] > A[i]:
        A[parent(i)], A[i] = A[i], A[parent(i)]
        i = parent(i)

def increase_key(A, i, key):
    """
        Input: A: an array representing a heap, i: an array index, key: a new key greater than A[i]
        Output: A still representing a heap where the key of A[i] was increased to key
        Running Time: O(log n) where n =heap-size[A]
    """
    if key < A[i]:
        raise Exception('New key must be larger than current key')
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def left(i):
    """
       Finding left leaf node position for a parent node

       :param int i: index of parent node
       :return int i: index in the heap
    """
    return 2 * i + 1


def right(i):
    """
       Finding right leaf node position for a parent node

       :param int i: index of parent node
       :return int i: index in the heap
    """
    return 2 * i + 2


def parent(i):
    """
       Finding leaf parent node

       :param int i: index of leaf node
       :return int i: index in the heap
    """
    return floor((i - 1) / 2)


if __name__ == '__main__':
  # Juni 15 Opgave 3
  # Efter IncreaseKey:  18 15 16 9 8 12 13 1 4
  # Efter ExtractMax:   16 15 13 9 8 12 4 1
  a = [18, 9, 16, 4, 8, 12, 13, 1, 2]

  increase_key(a, 9-1, 15)

  print(a)

  extractMax(a)

  print(a)

  # Juni 14 opgave 3 Efter Build-Max-Heap:  10 8 9 7 6 3 5 2 4 1

  a = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]

  buildMaxHeap(a)

  print(a)

  # Juni 16 opgave 3 Efter Build-Max-Heap:  9 8 7 4 2 6 5 1 3
  a = [2, 1, 5, 4, 8, 6, 7, 9, 3]

  buildMaxHeap(a)

  print(a)

  # juni 13 opgave 3 Efter insert in Min-heap: 1 2 5 4 2 6 6 9 8 7
  a = [2, 4, 5, 8, 7, 6, 6, 9]

  insert(a, 1)
  insert(a, 2)

  buildMinHeap(a)

  print(a)