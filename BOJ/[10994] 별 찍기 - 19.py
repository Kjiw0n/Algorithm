# 3일때 기준
# 홀수줄(*) -> 9 5 1
# 짝수줄( ) -> 7 3
# 짝수줄(* ) > 6 2

# 4일때 기준
# 홀수줄(*) -> 13 9 5 1
# 짝수줄( ) -> 11 7 3
# 짝수줄(* ) > 10 6 2 => 2 + 4 * (N // 2)

# 위 절반: odd는 -, even은 +
# 아래 절반: odd는 +, even은 -
# 위 절반: 1 + 2(N-1) 줄
# 아래 절반: 2(N-1) 줄
# -> 위 절반만 리스트에 저장 후 출력, 뒤에서부터 출력 !!

import sys

result_str = []
N = int(sys.stdin.readline())

# 1 5 9 13
# 총 1 + 4(N-1) 줄
tot = 1 + 4 * (N - 1)

half = (tot + 1) // 2

# !!중요한 건 어쨋든 총 1 + 4(N-1)개의 문자들.
def odd(n):
    edge_num = n - 1
    mid_num = tot - 4 * (edge_num)
    result = '* ' * edge_num + '*' * mid_num + ' ' + '* ' * edge_num
    return result

def even(n): # 이때 n은 짝수줄 중 n번째.. (2번째 줄이면 n=1, 4번째 줄 n=2...)
    star_num = n
    space_num = tot - (4 * n) + 1
    result = '* ' * star_num + ' ' * space_num + '* ' * star_num
    return result

for i in range(half):
    if i % 2 == 0:
        odd_line_num = i // 2 + 1
        result_str.append(odd(odd_line_num))
    else:
        even_line_num = i // 2 + 1
        result_str.append(even(even_line_num))

print(*result_str, sep='\n')
result_str.pop(half - 1)
print(*result_str[::-1], sep='\n')
