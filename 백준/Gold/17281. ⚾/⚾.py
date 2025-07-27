import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

innings = [list(map(int, input().split())) for _ in range(N)]

players = [i for i in range(1, 9)]

orders = []

for perm in permutations(players):
    order = list(perm[:3]) + [0] + list(perm[3:])
    orders.append(order)
    
def simulate(order, innings):
    score = 0
    batter_index = 0
    
    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0
        
        while out < 3:
            result = inning[order[batter_index]]
            
            if result == 0:
                out += 1 
            elif result == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif result == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif result == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            elif result == 4:
                score += b3 + b2 + b1 + 1
                b3, b2, b1 = 0, 0, 0
                
            batter_index = (batter_index + 1) % 9
            
    return score
    
max_score = 0

for order in orders:
    score = simulate(order, innings)
    if score > max_score:
        max_score = score
        
print(max_score)  
    