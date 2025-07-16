class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = len(points)
        points.sort(key = lambda x:x[0])
        prev = points[0]

        for each in range(1, len(points)):
            curr = points[each]

            if(curr[0] <= prev[1]):
                prev[1] = min(prev[1], curr[1])
                arrows-=1
            else:
                prev = curr

        return arrows
        
