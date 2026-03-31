import sys
from collections import deque

input = sys.stdin.readline

N, M, V =  map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
    
visited = [False] * (N+1)
visited2 = [False] * (N+1)

def BFS(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def DFS(start):
    visited2[start] = True
    print(start)
    for node in graph[start]:
        if not visited2[node]:
            DFS(node)

DFS(V)
BFS(V)
    