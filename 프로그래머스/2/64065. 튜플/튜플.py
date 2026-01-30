def solution(s):
    s = s[2:-2]
    s = s.split("},{")

    s_list = []
    for i in s:
        num = list(map(int, i.split(',')))
        s_list.append(num)

    s_list.sort(key=len)

    answer = []
    for s in s_list:
        for num in s:
            if num not in answer:
                answer.append(num)
    return answer