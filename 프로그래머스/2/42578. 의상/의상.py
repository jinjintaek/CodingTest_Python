def solution(clothes):
    count = {}
    for name, kind in clothes:
        if kind not in count:
            count[kind] = 2
        else:
            count[kind] += 1
    ways  = 1
    for cnt in count.values():
        ways *= cnt
    return ways -1