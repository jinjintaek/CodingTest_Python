import sys

input = sys.stdin.readline
numbers = [int(input()) for _ in range(9)]

max_number = 0
that_idx = 0
for idx, i in enumerate(numbers):
    if i > max_number:
        max_number = i
        that_idx = idx + 1
        
print(max_number)
print(that_idx)
        
