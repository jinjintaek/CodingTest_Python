import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = []

def recur(num, start):
    if num == m:
        print(*result)
        return
    for i in range(start, n+1):
        result.append(i)
        recur(num+1, i+1)
        result.pop()

recur(0,1)