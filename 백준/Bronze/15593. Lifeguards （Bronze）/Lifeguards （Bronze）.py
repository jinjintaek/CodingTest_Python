import sys

N = int(sys.stdin.readline().strip())

intervals = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    intervals.append([start, end])
    
timeline = [0] * 1001
for start, end in intervals:
    for t in range(start, end):
        timeline[t] = 1

total_covered = sum(timeline)

coverage = [0] * 1001

for start, end in intervals:
    for t in range(start, end):
        coverage[t] += 1

exclusive_list = []
for i in range(N):
    start, end = intervals[i]
    exclusive = 0 
    for t in range(start, end):
        if coverage[t] == 1:
            exclusive += 1
    exclusive_list.append(exclusive)

result = total_covered - min(exclusive_list)

print(result)