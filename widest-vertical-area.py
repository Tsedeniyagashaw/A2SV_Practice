class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        output = 0
        points.sort()
        res = 0
        for i in range(len(points) - 1):
            res = points[i + 1][0] - points[i][0]
            output = max(output, res)
        return output
        
