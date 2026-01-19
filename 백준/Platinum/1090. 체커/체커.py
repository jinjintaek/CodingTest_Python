N = int(input())
friends = [list(map(int, input().split())) for _ in range(N)]

x_coords = [x for x, y in friends]
y_coords = [y for x, y in friends]

answer = [float('inf')] * N

# 모든 (x, y) 조합을 만남 지점 후보로
for meet_x in x_coords:
    for meet_y in y_coords:
        distances = []
        for x, y in friends:
            distances.append(abs(x - meet_x) + abs(y - meet_y))
        distances.sort()
        
        # K명을 모으는 비용 갱신
        cost = 0
        for k in range(N):
            cost += distances[k]
            answer[k] = min(answer[k], cost)

print(' '.join(map(str, answer)))