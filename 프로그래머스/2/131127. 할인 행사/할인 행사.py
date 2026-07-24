from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    dic = dict(zip(want,number))

    for i in range(len(discount)):
        window = discount[i:i+10]
        if len(window) < 10:
            break
            
        if dic == Counter(window):
            answer += 1
    return answer