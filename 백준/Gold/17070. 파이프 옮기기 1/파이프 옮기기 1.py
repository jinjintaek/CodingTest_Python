import sys
sys.setrecursionlimit(100000)  # 재귀 제한 해제 (필요할 수 있음)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 메모이제이션 테이블: -1은 아직 계산되지 않았음을 의미
memo = [[[-1]*3 for _ in range(N)] for _ in range(N)]

# 방향별 이동 가능 목록
# (dy, dx, 이동 후 방향)
moves = {
    0: [(0, 1, 0), (1, 1, 2)],            # 가로 → 가로 or 대각선
    1: [(1, 0, 1), (1, 1, 2)],            # 세로 → 세로 or 대각선
    2: [(0, 1, 0), (1, 0, 1), (1, 1, 2)]  # 대각선 → 모두 가능
}

def dfs(y, x, dir):
    # 이미 계산한 값이 있다면 그대로 반환
    if memo[y][x][dir] != -1:
        return memo[y][x][dir]

    # 종료 조건: 목적지 도착
    if y == N - 1 and x == N - 1:
        return 1

    result = 0  # 현재 위치에서 가능한 모든 경로의 합

    for dy, dx, ndir in moves[dir]:
        ny = y + dy
        nx = x + dx

        # 범위 밖이면 무시
        if ny >= N or nx >= N:
            continue

        # 벽 체크
        if ndir == 2:  # 대각선은 3칸 다 체크
            if board[y][x+1] == 1 or board[y+1][x] == 1 or board[y+1][x+1] == 1:
                continue
        else:
            if board[ny][nx] == 1:
                continue

        result += dfs(ny, nx, ndir)

    memo[y][x][dir] = result  # 메모이제이션 저장
    return result

# 초기 위치: (0, 1) 방향: 가로(0)
print(dfs(0, 1, 0))