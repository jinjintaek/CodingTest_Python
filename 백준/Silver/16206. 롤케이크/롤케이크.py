import sys

N, M = map(int, sys.stdin.readline().split())
cakes = list(map(int, sys.stdin.readline().split()))

cake_count = 0
clean_cut_cake = []
dirty_cut_cake = []
for cake in cakes:
    if cake == 10:
        cake_count += 1
    elif cake > 10:
        if cake % 10 == 0:
            clean_cut_cake.append(cake)
        else:
            dirty_cut_cake.append(cake)
            
clean_cut_cake.sort()
dirty_cut_cake.sort()

while M > 0:
    if clean_cut_cake:
        if clean_cut_cake[0] // 10 - 1 > M:
            cake_count += M 
            M = 0 
        else:
            cake_count += clean_cut_cake[0] // 10
            M -= clean_cut_cake[0] // 10 - 1
        del clean_cut_cake[0]
    elif dirty_cut_cake:
        if dirty_cut_cake[0] // 10 > M:
            cake_count += M 
            M = 0 
        else:
            cake_count += dirty_cut_cake[0] // 10
            M -= dirty_cut_cake[0] // 10
        del dirty_cut_cake[0]
    
    else:
        break
print(cake_count)

