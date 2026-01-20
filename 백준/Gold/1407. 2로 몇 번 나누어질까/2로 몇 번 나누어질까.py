def sum_f(n):
    if n == 0:
        return 0
    
    total = n 
    
    power = 1 
    while power * 2 <= n:
        
        total += (n // (power * 2)) * power
        power *= 2
    
    return total

A, B = map(int, input().split())
print(sum_f(B) - sum_f(A-1))