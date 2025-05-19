import sys
from itertools import combinations as cb

def solution(M, card_list):
    max_sum = 0
    for a, b, c in cb(card_list, 3):
        if (a+b+c) > max_sum and (a+b+c) <= M:
            max_sum = a+b+c
    
    return max_sum

        
N, M = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))

print(solution(M, card_list))