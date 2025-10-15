import sys
T = int(sys.stdin.readline().strip())

PS = []

for _ in range(T):
    ps = sys.stdin.readline().strip()
    stack = []
    is_vps = True
    for c in ps:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                is_vps = False
                break
            else:
                stack.pop()
        
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")