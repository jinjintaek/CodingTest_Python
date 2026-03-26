import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
P = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(P):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (N+1)

def BFS(start):
    queue = deque([start])
    visited[start] = True
    count = 0
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                count += 1
    return count

print(BFS(1))