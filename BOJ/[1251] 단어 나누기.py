word = input()

result_list = []
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        result = word[:i][::-1] + word[i: j][::-1] + word[j:][::-1]
        result_list.append(result)

print(min(result_list))