class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
 larger_nums = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                        count += 1
            larger_nums.append(count)
                
        return larger_nums            

        
