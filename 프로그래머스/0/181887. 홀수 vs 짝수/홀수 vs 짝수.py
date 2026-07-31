def solution(num_list):
    even = 0
    odd = 0
    
    for i,v in enumerate(num_list):
        if i % 2 == 0:
            even += v
        else:
            odd += v
            
    return max(even,odd)