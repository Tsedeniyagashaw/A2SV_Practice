class Solution:
    def frequencySort(self, s: str) -> str:
        letter_count = Counter(s)
        sorted_letter = letter_count.most_common()
        res = "" 
        for letter,count in sorted_letter:
                res += letter * count
        return res        
                


            
               
