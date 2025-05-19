def solution(N, M, L):
    
    ball_count = [1] + [0] * (N-1)
    
    idx = 0
    
    while ball_count[idx] < M:

        if M == 1:
            return 0
            
        elif ball_count[idx] % 2 != 0:
            idx -= L
            if idx >= N:
                idx %= N
            elif idx < 0:
                idx += N
            ball_count[idx] += 1
            
        else:
            idx += L
            if idx >= N:
                idx %= N
            elif idx < 0:
                idx += N
            ball_count[idx] += 1
            
    return sum(ball_count) - 1
    
N, M, L = map(int, input().split())
print(solution(N, M, L))