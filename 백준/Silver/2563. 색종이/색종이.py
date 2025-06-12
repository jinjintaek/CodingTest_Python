import sys

N = int(sys.stdin.readline().strip())

array = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            array[i][j] = 1
            
result = 0
for i in range(100):
    result += array[i].count(1)
    
print(result)
    