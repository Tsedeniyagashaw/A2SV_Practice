class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = []
        seconds = 0
        person = 0
        
        for i in range(len(tickets)):
            queue.append(i)
        while queue:
            seconds += 1
            person = queue.pop(0)
            if tickets[person] >= 1:
                tickets[person] -= 1
            if  person == k and tickets[person] == 0:
                break 
            if  person != k and tickets[person] == 0:
                continue
            queue.append(person)

        return seconds               


        