class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = []
        index = 0
        for i in range(n):
            nums.append(i+1)

        while len(nums) > 1:
            index = (index + k - 1) % len(nums)
            nums.pop(index)
            i = index
        return  nums[0]   

           

           
