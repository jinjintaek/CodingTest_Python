def solution(myString):
    answer = []
    x_list = myString.split('x')
    for ch in x_list:
        answer.append(len(ch))
    return answer