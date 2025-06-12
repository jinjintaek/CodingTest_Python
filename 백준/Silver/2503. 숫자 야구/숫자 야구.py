import sys

N = int(sys.stdin.readline().strip())
question = []
for _ in range(N):
    q = list(map(int, sys.stdin.readline().split()))
    question.append(q)
candidate = [i for i in range(123, 988) if len(set(str(i))) == 3 and '0' not in str(i)]

answer = 0

for i in candidate:
    is_valid = True
    for q, s, b in question:
        str_i = str(i)
        str_q = str(q)
        strike = 0
        ball = 0
        for j in range(3):
            if str_i[j] == str_q[j]:
                strike += 1
            elif str_i[j] != str_q[j] and str_i[j] in str_q:
                ball += 1
        if strike != s or ball != b:
            is_valid = False
            break
    if is_valid:
        answer += 1

print(answer)