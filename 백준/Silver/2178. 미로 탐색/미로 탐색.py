import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]

dist = [[-1] * M for _ in range(N)]
dist[0][0] = 1


dy = [0,0,1,-1]
dx = [1,-1,0,0]

def BFS(y,x):
    queue = deque([(y,x)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if dist[ny][nx] == -1 and graph[ny][nx] == 1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny,nx))
    return

BFS(0,0)
print(dist[N-1][M-1])
                
    