def solution(board, moves):
    answer = 0
    dolls = []
    
    for move in moves:
        for b in board:
            if b[move -1] != 0:
                doll = b[move - 1]
                    
                if dolls and doll == dolls[-1]:
                    dolls.pop()
                    answer += 2
                    b[move -1] = 0
                    break
                else:
                    dolls.append(doll)
                    b[move -1] = 0
                    break
    return answer
                
    