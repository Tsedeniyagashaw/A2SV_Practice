class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        res = [[0] * cols for _ in range(rows)]
        for row_idx in range(rows):
          for col_idx in range(len(image[0]) - 1, -1, -1):
            res[row_idx][cols - 1 - col_idx] = 1 - image[row_idx][col_idx]
            
        return res         
