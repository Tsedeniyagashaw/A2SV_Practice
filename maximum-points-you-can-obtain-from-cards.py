class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l, r = 0, n - k
        card_sum = sum(cardPoints[r:])
        res = card_sum

        while r < n:
            card_sum += cardPoints[l]
            card_sum -= cardPoints[r]
            res = max(res, card_sum)
            l += 1
            r += 1
        return res    



        

          

        
