def solution(s):
    cnt = 0
    for ch in s:
        if cnt < 0:
            return False
        if ch == "(":
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        return True
    else:
        return False
                
            

    return True