import sys

L = int(sys.stdin.readline())
N = int(sys.stdin.readline())

rc = [0] * L

exp = 0
exp_i = 0

for i in range(1, N+1):
    P, K = map(int, sys.stdin.readline().split())

    if K - P + 1 > exp:
        exp = K - P + 1
        exp_i = i
    for j in range(P, K+1):
        if rc[j-1] == 0:
            rc[j-1] += i

print(exp_i)

real = 0
real_i = 0

for i in range(1, N+1):
    if rc.count(i) > real:
        real = rc.count(i)
        real_i = i

print(real_i)