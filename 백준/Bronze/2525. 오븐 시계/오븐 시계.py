import sys

input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())

total = a * 60 + b + c
print(total // 60 % 24, total % 60)