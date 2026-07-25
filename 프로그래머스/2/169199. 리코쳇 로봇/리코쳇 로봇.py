from collections import deque
def solution(board):
    
    n = len(board)
    m = len(board[0])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                start_y, start_x = i, j
                
    queue = deque([(start_y, start_x,0)])
    visited = [[False] * m for _ in range(n)]
    visited[start_y][start_x] = True
    
    while queue:
        y, x, moves = queue.popleft()
        if board[y][x] == 'G':
            return moves
        for i in range(4):
            ny, nx = y, x
            
            while 0<=ny+dy[i]<n and 0<=nx+dx[i]<m and board[ny + dy[i]][nx + dx[i]] != 'D':
                ny += dy[i]
                nx += dx[i]
            
            if not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny,nx,moves+1))
        
                
    
    return -1