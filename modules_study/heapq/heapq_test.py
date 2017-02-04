import heapq

# Heaps are binary trees for which every parent node has a value less than or equal
# to any of its children. This implementation uses arrays for which heap[k] <= heap[2*k+1] and
# heap[k] <= heap[2*k+2] for all k


h = []

heapq.heappush(h, 1)
heapq.heappop(h, 1)
heapq.heappushpop(h, 1)
heapq.heapspecify(h)
heapq.heapreplace(heap, 1)

heapq.nlargest(n, iterable, key=None) #sorted(iterable, key=key, reverse=True)[:n]
heapq.nsmallest(n, iterable, key=None) #sorted(iterable, key=key)[:n]

heapq.merge(*iterator)
