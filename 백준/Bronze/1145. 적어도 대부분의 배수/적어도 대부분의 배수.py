import sys

A, B, C, D, E = map(int, sys.stdin.readline().split())
num_list = [A, B, C, D, E]



for i in range(1,1000000):
    count = 0
    for j in num_list:
        if i % j == 0:
            count += 1
    if count >= 3:
        print(i)
        exit()