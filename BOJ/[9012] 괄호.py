N = int(input())

for _ in range(N):
    s_list = list(input())
    stack = []
    is_vps = True
    for s in s_list:
        if s == '(':
            stack.append(s)
        else:
            if not stack or stack.pop() != '(':
                is_vps = False
        # print(stack)
    if is_vps and not stack:
        print('YES')
    else:
        print('NO')


