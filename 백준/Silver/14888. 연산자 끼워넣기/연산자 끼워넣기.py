from itertools import permutations
N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))

totals = []
for perm in set(permutations(ops[0] * "+" + ops[1] * "-" + ops[2] * "*" + ops[3] * "/")):
    total = A[0]
    for i in range(N-1):
        if perm[i] == "+":
            total += A[i+1]
        elif perm[i] == "-":
            total -= A[i+1]
        elif perm[i] == "*":
            total *= A[i+1]
        else:
            if total < 0:
                total = -(abs(total) // A[i+1])
            else:
                total = total // A[i+1]
    
    totals.append(total)
            
print(max(totals))
print(min(totals))