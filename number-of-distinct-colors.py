class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
       res = []
       ballmap = defaultdict(int)
       colormap = defaultdict(list)


       for ball, color in queries:
            if ball in ballmap:
                colormap[ballmap[ball]].remove(ball)
                if not colormap[ballmap[ball]]:
                    del colormap[ballmap[ball]]
            ballmap[ball] = color 
            colormap[color].append(ball) 
            res.append(len(colormap))
       return res          
