import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

max_num = max(numbers)
min_num = min(numbers)

print(min_num, max_num)