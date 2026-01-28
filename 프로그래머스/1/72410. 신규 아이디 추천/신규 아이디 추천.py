def solution(new_id):
    
    answer = new_id.lower()
    
    result = ""
    for i in answer:
        if i.isalnum() or i in ['-','_','.']:
            result += i
    answer = result
    
    while '..' in answer:
        answer = answer.replace("..", ".")
    
    answer = answer.strip('.')
    
    if not answer:
        answer = "a"
        
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer