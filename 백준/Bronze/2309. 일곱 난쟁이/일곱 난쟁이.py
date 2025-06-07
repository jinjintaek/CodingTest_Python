import sys

array = []

for i in range(9):
    array.append(int(sys.stdin.readline().strip()))

array.sort()

sumh = sum(array)

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if sumh - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            sys.exit()
