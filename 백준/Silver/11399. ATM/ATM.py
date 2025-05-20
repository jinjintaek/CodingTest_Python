import sys

def solution(N, time_list):
    time_list.sort()
    total_time = []
    per_time = 0
    for i in time_list:
        per_time = per_time + i
        total_time.append(per_time)
    
    return sum(total_time)
        
N = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split()))

print(solution(N, time_list))