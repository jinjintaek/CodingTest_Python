a, b = map(int, input().split())

if b < 45:
    b = 60 - (45 - b)
    if a == 0:  
        a = 23
    else:
        a -= 1
else:
    b -= 45

print(a, b)