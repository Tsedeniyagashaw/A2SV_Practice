class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}

        for winner, loser in matches:
            losses[winner] = losses.get(winner,0)
            losses[loser] = losses.get(loser,0) + 1

        zero_lost = []
        one_lost = []

        for player, lost in losses.items():
            if lost == 0:
                zero_lost.append(player)
            elif lost == 1:
                one_lost.append(player)    
        return [sorted(zero_lost),sorted(one_lost)]        

