class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_set = sorted(set(nums))
        l = 0
        n = len(nums)
        res = n
        count = 0

        for r in range(n):
            while l < len(nums_set) and nums_set[l] < nums_set[r] + n:
                l += 1

            w = l - r
            res = min(res, n - w)
        return res                   

        