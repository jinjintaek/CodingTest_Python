import sys

input = sys.stdin.readline

N = int(input())

number = input().strip()

numl = []
for num in number:
    num = int(num)
    numl.append(num)
    
print(sum(numl))