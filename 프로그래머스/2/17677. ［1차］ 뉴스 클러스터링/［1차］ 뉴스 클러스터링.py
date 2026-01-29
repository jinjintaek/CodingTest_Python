def solution(str1, str2):
    A = []
    B = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i:i+2].lower())

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i:i+2].lower())

    if len(A) == 0 and len(B) == 0:
        return 65536
    else:

        b = B[:]
        count = 0

        for i in A:
            if i in b:
                count += 1
                b.remove(i)

        answer = int(count / (len(A) + len(B) -count) * 65536)
        return answer