import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def BFS(y,x):
    queue = deque([(y,x)])
    chk[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not chk[ny][nx] and graph[ny][nx] == 1:
                    queue.append((ny,nx))
                    chk[ny][nx] = True
    return

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    chk = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not chk[i][j]:
                BFS(i,j)
                cnt += 1
    print(cnt)
                
            