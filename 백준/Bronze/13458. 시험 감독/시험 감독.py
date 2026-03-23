import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


answer = N

for i in A:
    a = i - B
    aa = a / C
    if a > 0:
        answer += math.ceil(aa)
    
print(answer)