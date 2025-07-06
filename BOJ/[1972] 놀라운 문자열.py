# 단어 개수 <= 100
# 단어 길이 <= 80

arr = []

while True:
    s = input()
    if s == '*':
        break
    arr.append(s)

# 단어 길이 = n
# 0쌍은 n-1개
# 1쌍은 n-2개
# 2쌍은 n-3개
# -> n^2

ans = []

for a in arr:
    flag = True
    for d in range(1, len(a) - 1): # d-쌍
        flag = True
        a_dict = {}
        for i in range(len(a) - d):
            str1 = a[i] + a[i + d]
            if str1 in a_dict:
                flag = False
                break

            a_dict[str1] = 1
        if not flag:
            break

    if flag:
        ans.append(f"{a} is surprising.")
    else:
        ans.append(f"{a} is NOT surprising.")

for a in ans:
    print(a)

