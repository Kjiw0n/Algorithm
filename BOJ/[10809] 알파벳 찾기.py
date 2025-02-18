S = input()
arr = [-1] * 26 

for i in range(len(S)):
    ord_i = ord(S[i]) - ord('a')
    if arr[ord_i] == -1:
        arr[ord_i] = i

print(*arr)
