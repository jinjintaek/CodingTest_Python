from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1,n+1)]
for i in permutations(nums, m):
    print(*i)