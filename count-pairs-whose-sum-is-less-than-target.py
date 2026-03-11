class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            if nums[i] + nums[j] < target:
                count += 1
                j -= 1
            else:
                i += 1              
        return count       

        
