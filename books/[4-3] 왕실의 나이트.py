# s 17:30 (20분)
# e 17:50 (+0분)
#
# 8 x 8 체스판
# 나이트 하나밖에 없음
# 나이트는 L자 형태로만 이동
#
# list_location = [열(0, 1, 2, 3, ..., 7), 행(0, 1, 2, 3, ..., 7)]
# location = [열(1, 2, 3, ..., 8), 행(a, b, c, ..., h)]
#     -> 뒤집어도 상관 x
#     => a -> 1... 어떻게 대응시키지?
#         1. 딕셔너리 자료형?
#         2. (v) 아스키코드 - 97
#
case1 = [-2, -1]
case2 = [-2, 1]
case3 = [2, -1]
case4 = [2, 1]
case5 = [-1, -2]
case6 = [-1, 2]
case7 = [1, -2]
case8 = [1, 2]
# => 이동 총 경우의 수 8개

total_case = [case1, case2, case3, case4, case5, case6, case7, case8]

location = input()
list_location = [ord(location[0]) - 97, int(location[1]) - 1]

print(list_location)

count = 0
for case in total_case:
    is_move = False
    for i in range(2):
        after_mave = list_location[i] - case[i]
        if after_mave < 0 or after_mave >= 8:
            is_move = False
            break
        is_move = True
    if is_move:
        count += 1

print(count)