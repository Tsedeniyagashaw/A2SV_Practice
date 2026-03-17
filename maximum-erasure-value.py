class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        score = 0
        summ = 0
        unique = {}

        for i,n in enumerate(nums):
            if n in unique:
                while left < unique[n] + 1:
                    summ -= nums[left]
                    left += 1
            unique[n] = i
            summ += n
            score = max(score, summ)
        return score            







        
