import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

hmin = min(min(row) for row in graph)
hmax = max(max(row) for row in graph)

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(y,x, height,vstd):
    vstd[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n:
            if graph[ny][nx] > height and not vstd[ny][nx]:
                dfs(ny,nx,height,vstd)
    
def areacount(height):
    vstd = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and not vstd[i][j]:
                dfs(i,j, height,vstd)
                cnt += 1
    return cnt
    
result = [1]
for i in range(hmin, hmax+1):
    result.append(areacount(i))

print(max(result))