import sys

input = sys.stdin.readline

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, input().split())
d = sum(days[:x-1]) + y

print(week[d%7])