from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

iters = list(permutations(A))

answer = 0
for iter in iters:
    temp = 0
    for i in range(N-1):
        temp += abs(iter[i] - iter[i+1])
    if temp > answer:
        answer = temp
        
print(answer)