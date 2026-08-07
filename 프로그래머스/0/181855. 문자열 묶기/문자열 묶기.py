from collections import Counter
def solution(strArr):
    
    new_arr = map(len, strArr)
    counts = Counter(new_arr)
    
    return max(counts.values())