def solution(arr, n):
    l = len(arr)
    if l % 2 == 0:
        for idx in range(1,l,2):
            arr[idx] += n
    else:
        for idx in range(0,l,2):
            arr[idx] += n
    return arr