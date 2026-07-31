def solution(names):
    answer = []
    for i, v in enumerate(names):
        if i % 5 == 0:
            answer.append(v)
    return answer