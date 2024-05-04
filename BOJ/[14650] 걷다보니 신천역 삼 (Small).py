N = int(input())

arr = ['0', '1', '2']
# result_set = set()
result = 0

def find(s):
    if len(s) > N:
        return

    if len(s) == N and int(s) % 3 == 0:
        # print(s)
        # result_set.add(s)
        global result
        result += 1

    for a in arr:
        ns = s + a
        find(ns)


find('1')
find('2')

# print(result_set)
print(result)
