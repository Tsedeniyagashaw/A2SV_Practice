class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        duplicated = []
        for num in nums:
            d[num] = d.get(num,0) + 1
            if d[num] == 2:
                duplicated.append(num)
        return list(set(duplicated))            

        
