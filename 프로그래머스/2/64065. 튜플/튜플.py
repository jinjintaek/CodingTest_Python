def solution(s):
    s = s[2:-2]
    s = s.split("},{")

    s_list = []
    for i in s:
        s_list.append(i.split(','))

    s_list.sort(key=len)

    answer = []
    for s in s_list:
        for num in s:
            if int(num) not in answer:
                answer.append(int(num))
    return answer