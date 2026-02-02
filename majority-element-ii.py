class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements_count = {}
        n = len(nums)
        output = []

        for num in nums:
            elements_count[num] = elements_count.get(num,0) + 1

        for num in elements_count:
            if elements_count[num] > n//3:
                output.append(num) 
        return output        
