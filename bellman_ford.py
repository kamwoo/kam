import sys

inf = sys.maxsize
n, m= map(int, input().split())

destination = [inf]*(n+1)
tree = list([] for _ in range(n+1))

is_possible = True

def bellman(start):
    global is_possible

    destination[start] = 0
    for repeat in range(n):
        for i in range(1,n+1):
            for node, weight in tree[i]:
                new_weight = destination[i] + weight
                if new_weight < destination[node] and destination[i] != inf:
                    destination[node] = new_weight
                    if repeat == n-1:
                        is_possible= False
                    # 마지막째 반복에서도 작은것이 나오고 업데이트가 되는 것을 무한히 작아지는 것
for _ in range(m):
    u, v, w = map(int, input().split())
    tree[u].append([v, w])

bellman(1)

if not is_possible:
    print(-1)
else:
    for i in destination[2:]:
        print(i if i != inf else "-1")
