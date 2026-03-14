class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = 'aeiou'
        res = 0
        mp = defaultdict(lambda: 0)

        for i, ch in enumerate(word):
            if ch in vowels:
                mp[ch] += 1
                if i == 0 or word[i-1] not in vowels:
                    l = c = i
                while len(mp) == 5 and all(mp.values()):
                    mp[word[c]] -= 1
                    c += 1
                res += (c - l)  
            else:
                    mp.clear()
                    l = c = i + 1
        return res                   
                          

             


  
