def solution(t, p):
    target = int(p)
    count = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i+len(p)]) <= target:
            count += 1
    return count

