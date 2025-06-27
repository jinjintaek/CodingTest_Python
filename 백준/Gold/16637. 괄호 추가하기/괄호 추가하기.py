import sys

N = int(sys.stdin.readline())

f = sys.stdin.readline().strip()

num = []
op = []
for i in f:
    if i == "+" or i == "-" or i == "*":
        op.append(i)
    else:
        num.append(int(i))
        
def calc(a, op, b):
    a, b = int(a), int(b)
    if op == "+":
        return a + b
    elif op == "-":
        return a - b 
    elif op == "*":
        return a * b
        
max_result = -float('inf')

def dfs(idx, current_value):
    global max_result
    
    if idx >= len(op):
        max_result = max(max_result, current_value)
        return
    
    next_val = calc(current_value, op[idx], num[idx+1])
    dfs(idx + 1, next_val)
    
    if idx + 1 < len(op):
        if idx + 2 < len(num):
            temp = calc(num[idx+1], op[idx+1], num[idx+2])
            next_val = calc(current_value, op[idx], temp)
            dfs(idx + 2, next_val)
        
dfs(0, num[0])

print(max_result)
