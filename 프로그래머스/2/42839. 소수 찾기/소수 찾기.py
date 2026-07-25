from itertools import permutations

def solution(numbers):
    answer = 0
    candidates = []
    for length in range(1,len(numbers)+1):
        for p in permutations(numbers,length):
            num = int("".join(p))
            candidates.append(num)
    
    candidates = list(set(candidates))
    
    def is_prime(num):
        if num <2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    for i in candidates:
        if is_prime(i):
            answer += 1
    return answer