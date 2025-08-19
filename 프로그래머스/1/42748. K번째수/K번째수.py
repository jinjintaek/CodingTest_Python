def solution(array, commands):
    answer = []
    for i,j,k in commands:
        na = array[i-1:j]
        na.sort()
        answer.append(na[k-1])
    return answer