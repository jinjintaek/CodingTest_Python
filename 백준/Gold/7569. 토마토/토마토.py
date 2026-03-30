import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz,ny,nx))
                
                
max_day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                max_day = max(max_day, graph[i][j][k])
print(max_day-1)
                
                
                
                
                