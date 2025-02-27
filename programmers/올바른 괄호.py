def solution(s):
    stack = []
    for s in s:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False

    return True