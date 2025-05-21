import sys

A, B, C, D = map(int, sys.stdin.readline().split())
P, M, N = map(int, sys.stdin.readline().split())

def attack(person, A, B, C, D):
    
    attack_count = 0

    if person % (A+B) <= A and person % (A+B) != 0:
        attack_count += 1
    if person % (C+D) <= C and person % (C+D) != 0:
        attack_count += 1
    
    return attack_count
    

print(attack(P, A, B, C, D))
print(attack(M, A, B, C, D))
print(attack(N, A, B, C, D))