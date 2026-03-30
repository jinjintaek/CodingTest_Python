import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
                
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def BFS(y,x,island_number):
    queue = deque([(y,x)])
    graph[y][x] = island_number
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    graph[ny][nx] = island_number
                    visited[ny][nx] = True
                    queue.append((ny,nx))
  
island_number = 2                  
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            BFS(i, j, island_number)
            island_number += 1
            
def BFS2(y, x, island_num):                                                                                                                                                    
    queue = deque([(y, x, 0)])                                                                                                                                 
    visited2 = [[False] * N for _ in range(N)]                                                                                                                                 
    visited2[y][x] = True                                                                                                                                                      
    while queue:                                                                                                                                                               
        y, x, dist = queue.popleft()                                                                                                                                           
        for i in range(4):                                                                                                                                                     
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited2[ny][nx]:                                                                                                           
                if graph[ny][nx] == island_num:                                                                                                            
                    continue
                if graph[ny][nx] != 0:                                                                                                                         
                    return dist                                                                                                                                             
                visited2[ny][nx] = True
                queue.append((ny, nx, dist + 1))                                                                                                                               
    return float('inf')
                                                                                                                                                                             
min_bridge = float('inf')
for i in range(N):
    for j in range(N):                                                                                                                                                         
        if graph[i][j] >= 2:  
            min_bridge = min(min_bridge, BFS2(i, j, graph[i][j]))                                                                                                              
                                                                                                                                                                             
print(min_bridge)
            

        

                    
        
                
                