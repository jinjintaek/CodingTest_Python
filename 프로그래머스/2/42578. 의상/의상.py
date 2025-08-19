def solution(clothes):
    count = {}
    for name, kind in clothes:
        if kind not in count:
            count[kind] = 0
        count[kind] += 1
    ways  = 1
    for cnt in count.values():
        ways *= (cnt + 1)
    return ways -1