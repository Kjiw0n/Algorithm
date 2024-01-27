import sys

X, Y = sys.stdin.readline().split()

def Rev(n):
    return n[::-1]

add_result = int(Rev(X)) + int(Rev(Y))

result = int(Rev(str(add_result)))

print(result)