import heapq

li = [1,6,3,567,12]

heapq.heapify(li)

heapq.heappush(li, 67)

print(li)

heapq.heappop(li)
heapq.heappop(li)

print(li)