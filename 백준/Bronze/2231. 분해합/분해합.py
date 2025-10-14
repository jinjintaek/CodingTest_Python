import sys

N = int(sys.stdin.readline().strip())

def sum_digits(num):
    digits = []
    for n in str(num):
        digits.append(int(n))
    return sum(digits)
        
k = len(str(N))

S = max(1, N - 9*k)

M = 0
for i in range(S, N):
    if i + sum_digits(i) == N:
        M = i
        break
        
print(M)