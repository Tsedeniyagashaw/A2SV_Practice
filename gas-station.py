class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
         return -1      
        tank = current = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            current += gas[i] - cost[i]
            
            if current < 0:
                start = i + 1
                current = 0
                
        return start
        
