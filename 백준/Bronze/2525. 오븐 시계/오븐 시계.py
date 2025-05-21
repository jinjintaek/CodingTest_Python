# 입력 받기
A, B = map(int, input().split())  # 현재 시각 A(시), B(분)
C = int(input())  # 요리 시간 C(분)

# 총 분 계산
total_minutes = (A * 60 + B) + C

# 시(hour)와 분(minute) 계산
hour = (total_minutes // 60) % 24
minute = total_minutes % 60

# 결과 출력
print(hour, minute)