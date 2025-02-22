def solution(nums):
    N = len(set(nums))
    return min(N, len(nums) // 2)