def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left+right) // 2
        total = sum(mid//t for t in times)
        if total >= n:
            answer = mid
            right = mid - 1
        elif total < n:
            left = mid + 1
    
    return answer