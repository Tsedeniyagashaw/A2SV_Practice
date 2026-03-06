class Solution:
    def thirdMax(self, nums: List[int]) -> int:     
        nums = set(nums)
        nums = list(nums)
        nums.sort(reverse=True)
       
        for i in range(len(nums)):
            if len(nums) > 2:
                return nums[2]
            else:
                return nums[0]    
        
        
