class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] == 0:
                res.append([nums[i],nums[i + 1],nums[i + 2]])
        i += 1
        return res        
        
