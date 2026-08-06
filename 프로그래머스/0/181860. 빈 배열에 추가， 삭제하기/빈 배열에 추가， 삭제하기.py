def solution(arr, flag):
    answer = []
    for num, f in zip(arr,flag):
        if f:
            answer.extend([num]*num*2)
        else:
            answer = answer[:-num]
    return answer