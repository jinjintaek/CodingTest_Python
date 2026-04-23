def solution(s):
    s = s.split(' ')
    answer = [word.capitalize() for word in s]
    
    return ' '.join(answer)
