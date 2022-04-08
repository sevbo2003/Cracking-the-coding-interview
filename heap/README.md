# Heap 

- Also called a Priority Queue
- https://docs.python.org/3/library/heapq.html

```python
heapq.heapify(list)  # O(n*logn), in-place operation, min heap by default
heapq.heappush(heap, item)  # O(logn)
heapq._heapify_max(listForTree) # For a maxheap
heapq.heappop(heap)  # O(logn)
heapq._heappop_max(maxheap) # Pop from maxheap
heapq.nlargest(n, iterable, key=None) # O((n-k)*logn) to find the kth largest element
heapq.nsmallest(n, iterable, key=None)  

```
```python
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
