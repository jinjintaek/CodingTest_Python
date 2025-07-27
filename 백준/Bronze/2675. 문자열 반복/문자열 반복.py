import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    R, S = input().split()
    R = int(R)
    result = ''
    for char in S:
        result += char * R
    print(result)