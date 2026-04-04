import sys

input = sys.stdin.readline

l, c = map(int, input().split())

pw = input().split()
pw.sort()

result = []
def recur(num, start):
    if num == l:
        vowels = 'aeiou'
        vowel_cnt = sum(1 for c in result if c in vowels)
        consonant_cnt = l - vowel_cnt
        if vowel_cnt >= 1 and consonant_cnt >=2:
            print(''.join(result))
            return
    for i in range(start, c):
        result.append(pw[i])
        recur(num+1, i+1)
        result.pop()

recur(0,0)
            
    