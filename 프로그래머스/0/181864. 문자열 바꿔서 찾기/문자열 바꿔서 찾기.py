def solution(myString, pat):
    myString = myString.replace('A','X').replace('B','A').replace('X','B')
    if pat in myString:
        return 1
    else:
        return 0