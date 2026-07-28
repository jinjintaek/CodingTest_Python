def solution(arr):
    indices = [i for i,num in enumerate(arr) if num == 2]
    
    if not indices:
        return [-1]
    
    return arr[indices[0]:indices[-1]+1]