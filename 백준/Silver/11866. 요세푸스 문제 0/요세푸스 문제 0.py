import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())


numbers = deque(range(1,N+1))

ans = []

for _ in range(N):
    for _ in range(K-1):
        numbers.append(numbers.popleft())
    ans.append(numbers.popleft())
    
print(f"<{', '.join(map(str, ans))}>")