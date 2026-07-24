# 인덱스를 리스트에 담아서 반환하는 문제
# 만약 여러 부분 수열의 합이 같다? -> 짧은걸로
# 짧은 것도 여러개다? -> 먼저 나온걸로
# 이중 for문으로 해결 가능하지 않을까? 
# 

def solution(sequence, k):
    answer = []
    
    n = len(sequence)
    left = 0
    right = 0
    current_sum = sequence[0]
    
    min_len = float('inf')
    
    while right < n:
        if current_sum == k:
            current_len = right - left + 1
            
            if current_len < min_len:
                min_len = current_len
                answer = [left, right]
            
            current_sum -= sequence[left]
            left += 1
            
        elif current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]
                
        else:
            current_sum -= sequence[left]
            left += 1
    
    return answer