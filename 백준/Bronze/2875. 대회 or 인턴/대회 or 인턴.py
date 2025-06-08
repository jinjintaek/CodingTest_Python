import sys

N, M, K = map(int, sys.stdin.readline().split())

print(min(N//2, M, (N+M-K)//3))