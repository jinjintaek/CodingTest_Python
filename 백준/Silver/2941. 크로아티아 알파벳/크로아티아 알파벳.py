import sys

word = sys.stdin.readline().strip()
c_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
c_al_count = 0

for i in c_al:
    c_al_count += word.count(i)

answer = len(word) - c_al_count
print(answer)