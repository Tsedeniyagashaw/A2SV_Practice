class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n = len(nums)
        highest = 0
        for i in range(n):
            nums[i].sort()
        
        for j in range(len(nums[0])):  
            cols_max = 0
            for i in range(n):         
                cols_max = max(cols_max, nums[i][j])
            highest += cols_max  
        return highest        
