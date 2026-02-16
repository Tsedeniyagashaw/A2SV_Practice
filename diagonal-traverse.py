class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])
            
        diagonals = [[] for _ in range(rows + cols - 1 )]

        for i in range(rows):
            for j in range(cols):
                diagonals[i+j].append(mat[i][j])
        diag_arr = diagonals[0]

        for x in range(1, len(diagonals)):
            if x % 2 == 1:
                diag_arr.extend(diagonals[x])
            else:
                diag_arr.extend(diagonals[x][::-1])
        return diag_arr

                      
                    
