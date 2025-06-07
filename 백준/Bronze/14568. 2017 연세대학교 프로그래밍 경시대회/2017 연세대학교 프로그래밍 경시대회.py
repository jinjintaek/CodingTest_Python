import sys

N = int(sys.stdin.readline().strip())

N = N - 5
s = 0

for i in range(1, N+1, 2):
    s += ((N-i) // 2) + 1

print(s)