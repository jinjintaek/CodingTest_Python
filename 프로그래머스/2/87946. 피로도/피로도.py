from itertools import permutations
def solution(k, dungeons):
    # 던전 순서 순열 
    # 던전 방문 최대회수 업데이트
    # 던전을 못돌면 바로 현재 던전 수 기록
    max_cnt = 0
    
    for order in permutations(dungeons):
        cnt = 0
        current_k = k
        for dungeon in order:
            m, c = dungeon[0], dungeon[1]
            if current_k >= m:
                cnt += 1
                current_k -= c
            else:
                break
        
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt
            
                