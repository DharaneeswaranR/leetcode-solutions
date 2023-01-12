class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:       
        points.sort(key=lambda x: x[1])
        res = 1
        arrowpos = points[0][1]

        for start, end in points:
            if arrowpos >= start:
                continue
            else:
                res += 1
                arrowpos = end
        
        return res


"""
Approach: Overlapping intervals

"""