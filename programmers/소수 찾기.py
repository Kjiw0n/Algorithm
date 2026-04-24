from itertools import permutations
import math

def decimal(x):
    for i in range (2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)
    n = len(nums)
    perms = []
    for i in range(1, n + 1):
        perms += list(permutations(nums, i))
    
    nums_set = set()
    for perm in perms:
        s = ''
        for p in perm:
            s += p
        s = int(s)
        if s not in (0, 1):
            nums_set.add(s)
    
    cnt = 0
    for num in nums_set:
        if decimal(num): cnt += 1

    return cnt 