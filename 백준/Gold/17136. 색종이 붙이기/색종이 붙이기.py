import sys 

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]

def can_attach(y, x, size):
    if y + size > 10 or x + size > 10:
        return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if board[i][j] != 1:
                return False
    return True
    
def attach(y, x, size, value):
    for i in range(y, y + size):
        for j in range(x, x + size):
            board[i][j] = value
            
min_count = float('inf')
paper = [0] + [5] * 5

def dfs(pos, used):
    global min_count
    
    if used >= min_count:
        return 
    
    for i in range(pos, 100):
        y, x = divmod(i, 10)
        if board[y][x] == 1: 
            for size in range(5, 0, -1):
                if paper[size] > 0 and can_attach(y, x, size):
                    attach(y, x, size, 0)
                    paper[size] -= 1
                    dfs(i, used + 1)
                    attach(y, x, size, 1)
                    paper[size] += 1
            return
    min_count = min(min_count, used)
    
dfs(0, 0)
print(min_count if min_count != float('inf') else -1)
                