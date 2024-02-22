# s 01:11 (20분)
# e 01:21

N = int(input())

# 딕셔너리 자료형

array = dict()
for i in range(N):
    name, score = map(str, input().split())
    array[name] = int(score)

# sol1) 함수 이용
def setting(date):
    return date[1]

result = sorted(array, key=setting, reverse=True)

# sol2) lambda 이용
result1 = sorted(array, key = lambda data: data[1], reverse=True)

print(*result)
print(*result1)