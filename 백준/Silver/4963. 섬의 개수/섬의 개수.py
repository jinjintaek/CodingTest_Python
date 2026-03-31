import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

dy = [1,-1,0,0,1,1,-1,-1]
dx = [0,0,1,-1,1,-1,1,-1]

def dfs(y,x):
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<h and 0<=nx<w:
            if graph[ny][nx] == 1 and not vstd[ny][nx]:
                vstd[ny][nx] = True
                dfs(ny,nx)

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        exit(0)
    graph = [list(map(int,input().split())) for _ in range(h)]
    vstd = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not vstd[i][j]:
                vstd[i][j] = True
                dfs(i,j)
                cnt += 1
    print(cnt)
                


        