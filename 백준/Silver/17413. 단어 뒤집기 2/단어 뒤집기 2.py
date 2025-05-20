import sys

words = sys.stdin.readline().strip() + ' '

stack = []
tagtag = False
result = ""

for i in words:

    # 괄호를 만났을 때 
    if i == "<":
        for _ in range(len(stack)):
            result += stack.pop()
        tagtag = True
        result += '<'
    
    # 괄호가 끝날 때        
    elif i == ">":
        tagtag = False
        result += '>'
    
    # 괄호 안 문자열
    elif tagtag:
        result += i
        
    # 공백 (괄호 밖)
    elif i == ' ':
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
        
    # 괄호 밖 문자열
    else:
        stack.append(i)
            
print(result)