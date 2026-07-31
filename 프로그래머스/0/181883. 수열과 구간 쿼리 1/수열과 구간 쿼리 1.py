def solution(arr, queries):
    answer = []
    for s, e in queries:
        for idx in range(s,e+1):
            arr[idx] += 1
    return arr