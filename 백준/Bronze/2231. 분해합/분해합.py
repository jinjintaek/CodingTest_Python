import sys

N = int(sys.stdin.readline().strip())

M = 0
for i in range(max(0,N-len(str(N))*9),N):
    if sum(map(int,str(i))) + i == N:
        M = i 
        break

print(M)
