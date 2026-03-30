import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def BFS(start):
    queue = deque([start])
    dist = [0] * (N+1)
    visited = [False] * (N+1)
    visited[start]  = True
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                dist[next] = dist[node] + 1
                queue.append(next)
    return sum(dist)
  
kb = [] 
for i in range(1,N+1):
    kb.append(BFS(i))

print(kb.index(min(kb)) + 1)