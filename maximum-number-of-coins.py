class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        coins = 0
        for i in range(n//3,n,2):
            coins += piles[i]
        return coins    
        
