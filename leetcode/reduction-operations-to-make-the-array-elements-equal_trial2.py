class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        op = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                op += 1
            res += op
        return res        
       
       

       

        