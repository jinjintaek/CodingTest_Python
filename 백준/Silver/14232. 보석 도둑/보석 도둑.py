N = int(input())

i = 2
jewel = []
while  i <= int(N**0.5)+1:  
    while N % i == 0:  
        jewel.append(i)
        N = N // i
    i += 1

if N > 1:
    jewel.append(N)
    
print(len(jewel))
print(' '.join(map(str, jewel)))