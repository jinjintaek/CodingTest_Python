import sys
N = int(sys.stdin.readline().strip())
quizzes = []
for _ in range(N):
    quizzes.append(sys.stdin.readline().strip())


for quiz in quizzes:
    streak = 0
    points = 0
    for sym in quiz:
        if sym == "O":
            streak += 1
            points += streak
        else:
            streak = 0
    
    print(points)
            