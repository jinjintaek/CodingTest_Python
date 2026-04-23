import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9\-\_\.]','',answer)
    answer = re.sub('\.{2,}','.',answer)
    answer = answer.strip('.')
    if not answer:
        answer += 'a'
    if len(answer)>=16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer.rstrip('.')
    while len(answer) <= 2:
        answer += answer[-1]
    return answer
    
            