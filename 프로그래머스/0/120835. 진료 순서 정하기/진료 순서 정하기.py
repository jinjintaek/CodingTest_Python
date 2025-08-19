def solution(emergency):
    order = {}
    for i, v in enumerate(sorted(emergency, reverse=True)):
        order[v] = i + 1
    
    return [order[i] for i in emergency]