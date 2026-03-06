class Solution:
   
    def pancakeSort(self, arr: List[int]) -> List[int]:    
        n = len(arr)
        ans = []
        for max_num in range(n, 1, -1):
            index = arr.index(max_num)
            arr[:index + 1] = reversed(arr[:index+1])
            ans.append(index + 1)
            arr[:max_num] = reversed(arr[:max_num])
            ans.append(max_num)
        return ans    



                

         

        
        
