from itertools import combinations

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            homes.append((i,j))
        elif grid[i][j] == 2:
            chickens.append((i,j))

answer = float('inf')
for comb in combinations(chickens, M):
    total = 0
    for home in homes:
        min_dist = float('inf')
        for chicken in comb:
            dist = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            min_dist = min(min_dist, dist)
        total += min_dist
    answer = min(answer, total)

print(answer)