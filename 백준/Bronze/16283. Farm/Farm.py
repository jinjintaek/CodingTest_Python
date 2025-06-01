import sys

a, b, n, w = map(int, sys.stdin.readline().split())

cnt = 0

for i in range(1,n):
    x = i
    y = n - i
    
    if a*x + b*y == w:
        s = x 
        g = y
        cnt += 1 
        
if cnt == 1:
    print(s, g)
else:
    print(-1)