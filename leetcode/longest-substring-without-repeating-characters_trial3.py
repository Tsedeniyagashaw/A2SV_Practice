class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , right = 0,0
        dict_a = defaultdict(int)
        max_len = 0
        for right in range(len(s)):
                dict_a[s[right]] += 1
                while left < len(s) and len(dict_a) != (right - left + 1):
                    dict_a[s[left]] -= 1
                    if dict_a[s[left]] == 0:
                        del dict_a[s[left]]
                    left += 1
                max_len = max(max_len, right - left + 1)
                        
        return max_len   