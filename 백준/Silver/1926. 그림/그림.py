import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]


dy = [0,0,1,-1]
dx = [1,-1,0,0]

def BFS(y, x):
    queue = deque([(x,y)])
    chk[y][x] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0<= ny < n:
                if not chk[ny][nx] and graph[ny][nx] == 1:
                    chk[ny][nx] = True
                    count += 1
                    queue.append((nx,ny))
    return count
          

cnt = 0
mp = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not chk[i][j]:
            mp = max(mp, BFS(i,j))
            cnt +=1 
        
print(cnt)
print(mp)