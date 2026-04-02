import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())

ngraph = [list(input().strip()) for _ in range(n)]
bgraph = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if ngraph[i][j] == 'G' or ngraph[i][j] == 'R':
            bgraph[i][j] = 'R'
        else:
            bgraph[i][j] = 'B'
            
vstd = [[False] * n for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(y,x,graph,value):
    vstd[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n:
            if graph[ny][nx] == value and not vstd[ny][nx]:
                dfs(ny,nx,graph,value)
    

cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if not vstd[i][j]:
            dfs(i,j, ngraph,ngraph[i][j])
            cnt += 1
result.append(cnt)
cnt = 0
vstd = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not vstd[i][j]:
            dfs(i,j, bgraph,bgraph[i][j])
            cnt += 1
result.append(cnt)
            
print(*result)

            