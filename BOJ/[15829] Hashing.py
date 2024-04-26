L = int(input())
s = input()

sum = 0
for i in range(L):
    sum += (ord(s[i]) - 96) * 31 ** i

print(sum % 1234567891)
