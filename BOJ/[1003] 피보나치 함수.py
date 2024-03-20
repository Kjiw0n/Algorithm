T = int(input())

arr = []
for i in range(T):
    arr.append(int(input()))

dp_0 = [0] * (max(arr) + 4)
dp_0[0] = 1
dp_0[1] = 0
dp_0[2] = 1

def fibo_0(n):
    if n > 2 and dp_0[n] == 0:
        dp_0[n] = fibo_0(n - 1) + fibo_0(n - 2)

    return dp_0[n]

dp_1 = [0] * (max(arr) + 4) # 여기서 dp는 0, 1이 리턴되는 횟수가 저장됨
dp_1[0] = 0
dp_1[1] = 1
dp_1[2] = 1

def fibo_1(n):
    if n > 2 and dp_1[n] == 0:
        dp_1[n] = fibo_1(n - 1) + fibo_1(n - 2)

    return dp_1[n]

result = []

for a in arr:
    result.append([fibo_0(a), fibo_1(a)])


for r in result:
    print(*r)