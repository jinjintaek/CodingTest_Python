import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [0] * 100001


queue = deque([N])
while queue:
    x = queue.popleft()
    nxs = [x+1, x-1 , x*2]
    for nx in nxs:
        if 0 <= nx <=100000:
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)
if N == K:
    print(0)
else:
    print(visited[K])