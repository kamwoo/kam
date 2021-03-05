import sys

n = int(input())
m = int(input())

inf = sys.maxsize
destination = list([inf]*n for _ in range(n))

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and destination[i][j] > destination[i][k]+destination[k][j]:
                    destination[i][j] = destination[i][k] +destination[k][j]

for _ in range(m):
    a, b, c = map(int,input().split())
    if destination[a-1][b-1] > c:
        destination[a-1][b-1] = c

floyd()

for i in destination:
    for j in i:
        if j==inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()