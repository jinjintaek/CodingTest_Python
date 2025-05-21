import sys

N = int(sys.stdin.readline())

result = 0 

for i in range(1, N+1):
    for j in range(i, N//i + 1):
        result += 1
        
print(result)

# ----------- 시간 초과했던 답 --------------
# N = int(sys.stdin.readline())

# def c_count(N):
#     count = 0
    
#     for i in range(1, int(N**0.5) + 1):
#         if N % i == 0:
#             count += 2 if i != N // i else i 
#     return count

# def solution(N):
#     result = 0
#     for i in range(1, N+1):
#         if c_count(i) % 2 == 0:
#             result += (c_count(i) // 2)
#         elif c_count(i) % 2 != 0:
#             result += ((c_count(i) + 1) // 2)
            
#     return result
    

# print(solution(N))
