def solution(t, p):
    target = int(p)
    
    cnt = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i+len(p)]) <= target:
            cnt += 1
    
    return cnt