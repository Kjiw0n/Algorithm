# 방학 L일
# 국어 총 Ap / 하루 Cp (올림)
# 수학 총 Bp / 하루 Dp (올림)
# -> max 값
import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean_day = math.ceil(A / C)
math_day = math.ceil(B / D)

tot_study_day = max(korean_day, math_day)
result = L - tot_study_day

print(result)
