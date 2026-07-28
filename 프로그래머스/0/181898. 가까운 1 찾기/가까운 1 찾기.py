def solution(arr, idx):
    answer = 0
    for i, v in enumerate(arr[idx:]):
        if v == 1:
            answer = i + idx
            return answer
    return -1