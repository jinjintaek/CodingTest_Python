import sys

A, B = map(int, sys.stdin.readline().split())

first = int((-(2*A) + ((2*A)**2-4*B)**0.5) / 2)
second = int((-(2*A) - ((2*A)**2-4*B)**0.5) / 2)

if first > second:
    print(second, first)
elif first < second:
    print(first, second)
else:
    print(first)