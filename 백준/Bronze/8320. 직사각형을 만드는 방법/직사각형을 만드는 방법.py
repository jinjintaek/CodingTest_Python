import sys

N = int(sys.stdin.readline())

result = 0 

for i in range(1, N+1):
    for j in range(i, N//i + 1):
        result += 1
        
print(result)
       