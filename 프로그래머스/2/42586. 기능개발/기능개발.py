import math
def solution(progresses, speeds):
    answer = []
    left = []
    
    for progress, speed in zip(progresses,speeds):
        left.append(math.ceil((100-progress)/speed))
        
    current = left[0]
    cnt = 1
    
    for d in left[1:]:
        if d <= current:
            cnt += 1
        else:
            answer.append(cnt)
            current = d
            cnt = 1
    
    answer.append(cnt)
        
    return answer