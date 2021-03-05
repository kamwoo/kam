import heapq
import sys

inf = sys.maxsize
V,E = map(int, input().split())
k = int(input())

tree = list([] for _ in range(V+1))
destination = [inf]*(V+1)
heap = []

def dijkstra(start):
    destination[start] = 0
    heapq.heappush(heap, [0,start])
    while heap:
        w, n = heapq.heappop(heap)
        for node, distance in tree[n]:
            new_distance = w + distance
            if new_distance < destination[node]:
                destination[node] = new_distance
                heapq.heappush(heap, [new_distance, node])

for _ in range(E):
    u, v, w = map(int, input().split())
    tree[u].append([v,w])

dijkstra(k)

for i in destination[1:]:
    print(i if i != inf else "INF")