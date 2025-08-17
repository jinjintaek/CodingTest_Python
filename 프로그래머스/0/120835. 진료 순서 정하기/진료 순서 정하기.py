def solution(emergency):
    a = sorted(emergency, reverse=True)
    order = []
    for i in emergency:
        for j in a:
            if i == j:
                order.append(a.index(j)+1)
    return order