keypad = {1:(0,0), 2:(0,1), 3:(0,2), 
          4:(1,0), 5:(1,1), 6:(1,2), 
          7:(2,0), 8:(2,1), 9:(2,2),
         '*':(3,0), 0:(3,1), '#':(3,2)}

def solution(numbers, hand):
    lpo = keypad['*']
    rpo = keypad['#']
    answer = ""
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            lpo = keypad[i]
        elif i in [3,6,9]:
            answer += "R"
            rpo = keypad[i]
        else:
            if (abs(keypad[i][0] - lpo[0]) + abs(keypad[i][1] - lpo[1])) > (abs(keypad[i][0] - rpo[0]) + abs(keypad[i][1] - rpo[1])):
                answer += "R"
                rpo = keypad[i]
            elif (abs(keypad[i][0] - lpo[0]) + abs(keypad[i][1] - lpo[1])) < (abs(keypad[i][0] - rpo[0]) + abs(keypad[i][1] - rpo[1])):
                answer += "L"
                lpo = keypad[i]
            else:
                if hand == "right":
                    answer += "R"
                    rpo = keypad[i]
                else:
                    answer += "L"
                    lpo = keypad[i]
                
    return answer
            