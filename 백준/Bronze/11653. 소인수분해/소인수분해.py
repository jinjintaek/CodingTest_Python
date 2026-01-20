N = int(input())

i = 2
while  i <= int(N**0.5)+1:  
    while N % i == 0:  
        print(i)
        N = N // i
    i += 1

if N > 1:
    print(N)