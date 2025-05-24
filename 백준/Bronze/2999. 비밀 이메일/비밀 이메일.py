import sys

word = sys.stdin.readline().strip()
N = len(word)

R, C = 0, 0

for x in range(1, N+1):
    for y in range(x, N+1):
        if x * y == N:
            R, C = x, y
            
ans = ""
for i in range(R):
    ans += word[i::R]
    
print(ans)