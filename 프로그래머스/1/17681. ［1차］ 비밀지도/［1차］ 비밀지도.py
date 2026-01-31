def solution(n, arr1, arr2):
    arr1b = []
    arr2b = []
    for i in arr1:
        arr1b.append(format(i, f'0{n}b'))

    for i in arr2:
        arr2b.append(format(i, f'0{n}b'))


    answer = [] 
    for i,j in zip(arr1b, arr2b):
        line = ""
        for a, b in zip(i,j):
            if a == '1' or b == '1':
                line += "#"
            else:
                line += " "
        answer.append(line)
    return answer