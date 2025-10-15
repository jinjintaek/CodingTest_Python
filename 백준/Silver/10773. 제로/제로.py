import sys

K = int(sys.stdin.readline().strip())
numbers = []
for _ in range(K): 
    num = int(sys.stdin.readline().strip())
    numbers.append(num)

ans = []
for i in numbers:
    if i == 0:
        ans.pop()
    else:
        ans.append(i)

print(sum(ans))