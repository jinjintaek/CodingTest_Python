from itertools import permutations

def solution(expression):
    
    number = ""
    numbers = []
    operators = []
    
    for i in expression:
        if i.isdigit():
            number += i
        else:
            operators.append(i)
            numbers.append(int(number))
            number = ""
    
    numbers.append(int(number))
    
    op_set = set(operators)
    priorities = list(permutations(op_set))
    
    result = []
    for priority in priorities:
        num = numbers[:]
        ops = operators[:]
        
        for op in priority:
            i = 0
            while i < len(ops):
                if ops[i] == op:
                    num[i] = eval(str(num[i]) + op + str(num[i+1]))
                    num.pop(i+1)
                    ops.pop(i)
                else:
                    i += 1
        
        result.append(abs(num[0]))
    return(max(result))

            
    