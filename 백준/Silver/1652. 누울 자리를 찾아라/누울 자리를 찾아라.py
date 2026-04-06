import sys

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

cnt1 = 0
cnt2 = 0

for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] == '.':
            count += 1
            if count == 2:
                cnt1 += 1
        else:
            count = 0
            
for i in range(n):
    count = 0
    for j in range(n):
        if graph[j][i] == '.':
            count += 1
            if count == 2:
                cnt2 += 1
        else:
            count = 0
                
print(cnt1, cnt2)