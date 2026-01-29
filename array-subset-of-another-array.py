class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        d = dict()
        
        for i in a:
            d[i] = d.get(i,0) + 1
            
        for i in b:
            if i not in d or d[i] == 0:
                return False
            else:
                d[i] -= 1
                
        
        return True
    
    
    
