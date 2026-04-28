from collections import deque
def solution(maps):
    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    def bfs(y,x):
        queue = deque([(y,x)])
        
        while queue:
            y, x = queue.popleft()
            if y == len(maps) - 1 and x == len(maps[0]) - 1:
                return maps[y][x]
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<len(maps) and 0<=nx<len(maps[0]):
                    if maps[ny][nx] == 1:
                        maps[ny][nx] = maps[y][x] + 1
                        queue.append((ny,nx))
                        
        return -1
    
    
        
        
        
        
    return bfs(0,0)