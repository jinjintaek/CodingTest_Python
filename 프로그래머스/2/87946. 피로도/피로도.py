from itertools import permutations
def solution(k, dungeons):
    # 던전 순서 순열 
    # 던전 방문 최대회수 업데이트
    # 던전을 못돌면 바로 현재 던전 수 기록
    max_cnt = 0
    
    for order in permutations(dungeons, len(dungeons)):
        ck = k
        cnt = 0
        for dg in order:
            n = dg[0]
            s = dg[1]
            if ck >= n:
                ck = ck - s
                cnt += 1
            else:
                break
        
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt
                