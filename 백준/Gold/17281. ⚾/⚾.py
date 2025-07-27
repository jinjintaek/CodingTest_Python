import sys

input = sys.stdin.readline

N = int(input())

innings = [list(map(int, input().split())) for _ in range(N)]

max_score = 0

def simulate(order):
    score = 0
    batter_idx = 0
    
    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0
        
        while out < 3:
            result = inning[order[batter_idx]]

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

            batter_idx = (batter_idx + 1) % 9

    return score

def backtrack(depth, order, visited):
    global max_score
    
    if depth == 9:
        score = simulate(order)
        max_score = max(max_score, score)
        return
    
    if depth == 3:
        order.append(0)
        backtrack(depth + 1, order, visited)
        order.pop()
    
    else:
        for i in range(1, 9):
            if not visited[i]:
                visited[i] = True
                order.append(i)
                backtrack(depth + 1, order, visited)
                order.pop()
                visited[i] = False

visited = [False] * 9
backtrack(0, [], visited)
print(max_score)