class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        n = len(chars)
        index = 0
        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[index] = chars[i]
            index += 1
            if j - i > 1:
                count = str(j - i)
                for c in count:
                    chars[index] = c
                    index += 1
            i = j
        return index      
            

       
