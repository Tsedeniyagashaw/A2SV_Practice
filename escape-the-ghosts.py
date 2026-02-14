class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) +  abs(target[1])
        for i in ghosts:
            dist_ghost = abs(target[0] - i[0]) + abs(target[1] -i[1])
            if dist_ghost <= distance:
                return False
            return True    
