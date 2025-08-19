import math
def solution(progresses, speeds):
    left = []
    days = []
    for per in progresses:
        left.append(100-per)
    for per, speed in zip(left, speeds):
        days.append(math.ceil(per/speed))
    answer = []
    cur = days[0]
    cnt = 1
    
    for d in days[1:]:
        if d <= cur:
            cnt += 1
        else:
            answer.append(cnt)
            cur = d
            cnt = 1
    answer.append(cnt)
    return answer
    
        
        
        