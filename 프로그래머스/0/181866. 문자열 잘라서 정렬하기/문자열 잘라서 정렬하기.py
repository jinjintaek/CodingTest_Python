def solution(myString):
    answer = []
    return [ch for ch in sorted(myString.split('x')) if ch]