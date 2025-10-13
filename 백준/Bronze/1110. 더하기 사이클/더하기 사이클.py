N = input()

if len(N) < 2:
    N = "0" + N

originN = N
count = 0
while True:
    N = N[-1] + str(int(N[0]) + int(N[-1]))[-1]
    count += 1
    if N == originN:
        break

print(count)