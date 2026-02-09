class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        difference = 0
        swap = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
              difference += 1
              if difference > 2:
                return False
              swap.append([s1[i],s2[i]])
        if difference == 2:
          if swap[0][0] == swap[1][1] and swap[0][1] == swap[1][0]:   
              return True
          else:
              return False
        return difference == 0      

        
