class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = [0]

        for i in range(1,n):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
        res = 0        
        for i in range(n-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                j = stack.pop()
                res = max(res,i - j)
        return res                
