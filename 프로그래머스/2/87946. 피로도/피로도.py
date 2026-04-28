def solution(k, dungeons):
    max_cnt = 0
    for order in permutations(dungeons, len(dungeons)):
        current_k = k
        cnt = 0
        for dg in order:
            n = dg[0]
            s = dg[1]
            if current_k >= n:
                current_k -= s
                cnt += 1
            else:
                break
        
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt
            
                
    
    return max(answer)

from itertools import permutations