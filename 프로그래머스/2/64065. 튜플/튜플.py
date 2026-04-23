def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    answer = []
    for i in s:
        nums = i.split(',')
        for j in nums:
            if int(j) not in answer:
                answer.append(int(j))
        
    
    
        
        
        
    return answer
    
                