import heapq

a = [18, 9, 16, 4, 8, 12, 13, 1, 2]

def increaseKey(arr, value, newValue):
  for i, val in enumerate(a):
    if val == value:
      a[i] = newValue
  return arr

#print(increaseKey(a, 9, 15))

#heapq._siftup_max(a, 1)
#heapq._siftup(a, 1)
#heapq._siftdown(a, 9 - 1, 15) # decrease key

#heapq.heapify(a)             # for a min heap
heapq._heapify_max(a)        # for a maxheap!!

print(a)

heapq._heappop_max(a) # extract max!

print(a)