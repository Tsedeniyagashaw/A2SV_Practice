class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        conn = {}

        for i in range(len(list1)):
            conn[list1[i]] = i
        least = float("inf")

        
        for j in range(len(list2)):
            if list2[j] in conn:
                sum = j + conn[list2[j]]
                if sum < least:
                    least = sum
                    res = []
                    res.append(list2[j])
                elif sum == least:
                    res.append(list2[j])
        return res                    

        
