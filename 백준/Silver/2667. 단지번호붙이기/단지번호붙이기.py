import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = deque([(x,y)])
    visited[y][x] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    count += 1
    return count
    
cnt = 0
vil = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            vil.append(BFS(j,i))
            cnt += 1
vil.sort()         
print(cnt)
for i in vil:
    print(i)