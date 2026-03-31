import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

m, n, k = map(int, input().split())

graph = [[1] * n for _ in range(m)]
vstd = [[False] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1,y2):
        for x in range(x1, x2):
            graph[y][x] = 0
            
temp = 0
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(y,x):
    global temp
    temp += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<m and 0<=nx<n:
            if graph[ny][nx] == 1 and not vstd[ny][nx]:
                vstd[ny][nx] = True
                dfs(ny,nx)
    

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not vstd[i][j]:
            vstd[i][j] = True
            temp = 0
            dfs(i,j)
            result.append(temp)

result.sort()
print(len(result))
print(*result)
    

        