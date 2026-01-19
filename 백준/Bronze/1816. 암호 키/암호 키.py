TC = int(input())

for _ in range(TC):
    number = int(input())
    
    for i in range(2,1000001):
        if number % i == 0:
            print("NO")
            break
        if i == 1000000:
            print("YES")