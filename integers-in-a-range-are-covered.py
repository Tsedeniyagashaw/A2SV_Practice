class Solution(object):
    def isCovered(self, ranges, left, right):
      
        for i in range(left, right + 1):
            for start, end in ranges:
                if start <= i <= end:
                    break
            else:
                return False
        return True

                
                     
        
