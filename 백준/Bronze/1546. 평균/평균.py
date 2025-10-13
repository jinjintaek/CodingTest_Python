import sys
N = int(sys.stdin.readline().strip())
score = list(map(int, sys.stdin.readline().split()))

max_score = max(score)

new_score = []

for num in score:
    new_score.append(num/max_score*100)
    

print(sum(new_score) / N)