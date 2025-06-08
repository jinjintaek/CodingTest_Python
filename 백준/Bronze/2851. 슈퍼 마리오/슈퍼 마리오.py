import sys

array = []

for i in range(10):
    array.append(int(sys.stdin.readline().strip()))
    
gap = 100000
best = 0
for i in range(len(array)):
    if abs(sum(array[:i+1])- 100) <= gap:
        gap = abs(sum(array[:i+1])- 100)
        best = sum(array[:i+1])
        
print(best)