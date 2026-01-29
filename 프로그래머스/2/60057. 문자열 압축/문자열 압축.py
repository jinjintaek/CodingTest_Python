def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[:i]
        count = 1
        
        for j in range(i, len(s), i):
            current = s[j:j+i]
            
            if prev == current:
                count += 1
            else:
                if count != 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                
                prev = current
                count = 1
        
        if count != 1:
            compressed += (str(count) + prev)
        else:
            compressed += prev
        
        answer = min(answer, len(compressed))
        
    return answer