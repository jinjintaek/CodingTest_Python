def solution(want, number, discount):
    answer = 0

    
    for idx in range(len(discount) - 9):
        current = number[:]
        
        for item in discount[idx:idx+10]:
            if item in want:
                current[want.index(item)] -= 1
                
        if all(cnt <= 0 for cnt in current):
            answer += 1
            
    return answer