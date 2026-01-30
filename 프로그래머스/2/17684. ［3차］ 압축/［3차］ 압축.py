def solution(msg):
    dictionary = {}
    for i in range(26):
        dictionary[chr(ord('A')+i)] = i + 1

    answer = []
    w = ""
    next_code = 27
    for c in msg:
        if w + c in dictionary:
            w = w + c
        else:
            answer.append(dictionary[w])
            dictionary[w+c] = next_code
            next_code += 1
            w = c
    answer.append(dictionary[w])
    
    return answer