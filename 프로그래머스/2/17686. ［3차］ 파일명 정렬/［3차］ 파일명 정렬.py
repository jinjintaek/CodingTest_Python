def solution(files):
    parsed = []

    for idx, file in enumerate(files):
        for i, ch in enumerate(file):
            if ch.isdigit():
                head_end = i 
                break
        
        num_end = len(file)
        for i in range(head_end, len(file)):
            if not file[i].isdigit():
                num_end = i
                break

        parsed.append((file[:head_end].lower(), int(file[head_end:num_end]),idx, file))

    parsed.sort()


    return[x[3] for x in parsed]