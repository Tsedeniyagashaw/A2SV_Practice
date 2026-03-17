class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        same = 0
        right, left = 0, 0
        res = 0

        while right < n:
            same += freq.get(nums[right], 0)
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while same >= k:
                res += n - right
                freq[nums[left]] -= 1
                same -= freq[nums[left]]
                left += 1
            right += 1
        return res        



                 
        















