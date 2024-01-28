import sys

T = int(sys.stdin.readline())

charge = [25, 10, 5, 1]
test_case = [0] * T

for i in range(T):
    test_case[i] = int(sys.stdin.readline())

for i in range(T):
    result = [0] * len(charge)
    for j in range(len(charge)):
        result[j] = int(test_case[i] // charge[j])
        test_case[i] = test_case[i] % charge[j]

    print(*result)