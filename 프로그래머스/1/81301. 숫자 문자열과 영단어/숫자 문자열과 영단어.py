def solution(s):
    words = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
    for key, value in words.items():
        if value in s:
            s = s.replace(value, str(key))
            
    return int(s)