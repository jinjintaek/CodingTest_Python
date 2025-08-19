def solution(sizes):
    for i in range(len(sizes)):
        g, s = sizes[i]
        if g < s:
            sizes[i] = [s, g]
        
    max_g = max(g for g, s in sizes)
    max_s = max(s for g, s in sizes)
    
    return max_g * max_s