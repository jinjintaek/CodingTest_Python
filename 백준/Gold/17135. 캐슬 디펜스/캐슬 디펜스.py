import sys
import copy
from itertools import combinations
input = sys.stdin.readline

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

archer_positions = list(combinations(range(M), 3))

def find_target(board, archer_col):
    min_dist = float('inf')
    target = None
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                dist = abs(len(board) - y) + abs(archer_col - x)
                if dist <= D:
                    if dist < min_dist:
                        min_dist = dist
                        target = (y, x)
                    elif dist == min_dist and x < target[1]:
                        target = (y, x)
    
    return target

def simulate(board, archers):
    kill = 0
    
    for _ in range(N):
        targets = set()
        
        for archer_col in archers:
            target = find_target(board, archer_col)
            if target:
                targets.add(target)
                
        for y, x in targets:
            if board[y][x] == 1:
                board[y][x] = 0
                kill += 1
        
        board.pop()
        board.insert(0, [0]*M)
        
    return kill

max_kill = 0

for archers in archer_positions:
    temp_board = copy.deepcopy(board)
    
    kill_count = simulate(temp_board, archers)
    
    max_kill = max(max_kill, kill_count)
    
print(max_kill)