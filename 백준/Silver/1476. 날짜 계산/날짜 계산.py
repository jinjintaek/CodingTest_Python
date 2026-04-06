import sys

input = sys.stdin.readline


e, s, m = map(int, input().split())

for year in range(1, 15*28*19+1):
    if year%15 == e%15 and year % 28 == s%28 and year %19 == m%19:
        print(year)
        break
