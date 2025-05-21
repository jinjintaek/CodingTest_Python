a, b, c = map(int, input().split())
if a == b == c:
    상금 = 10000 + a * 1000
    print(상금)

elif a == b:
    상금 = 1000 + a * 100
    print(상금)

elif b == c:
    상금 = 1000 + b * 100
    print(상금)

elif a == c:
    상금 = 1000 + a * 100
    print(상금)

else:
    상금 = max(a,b,c) * 100
    print(상금)
