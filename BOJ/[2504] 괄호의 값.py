S = list(input())

def sol(S):
    stack = []
    for s in S:
        n = 0

        if s == ')':
            while stack and isinstance(stack[-1], int):
                n += stack.pop()
            if stack and stack.pop() == '(':
                if n > 0:
                    stack.append(n * 2)
                else:
                    stack.append(2)
            else:
                return 0
        elif s == ']':
            while stack and isinstance(stack[-1], int):
                n += stack.pop()
            if stack and stack.pop() == '[':
                if n > 0:
                    stack.append(n * 3)
                else:
                    stack.append(3)
            else:
                return 0
        # 여는 괄호
        else:
            stack.append(s)

    for x in stack:
        if not isinstance(x, int):
            return 0

    return sum(stack)

print(sol(S))