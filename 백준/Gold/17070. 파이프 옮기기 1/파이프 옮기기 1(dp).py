N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            continue
        
        if x - 1 >= 0:
            dp[y][x][0] += dp[y][x-1][0] + dp[y][x-1][2]
            
        if y - 1 >= 0:
            dp[y][x][1] += dp[y-1][x][1] + dp[y-1][x][2]
            
        if x - 1 >= 0 and y - 1 >= 0:
            if board[y-1][x] == 0 and board[y][x-1] == 0:
                dp[y][x][2] += dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]
                
print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])
