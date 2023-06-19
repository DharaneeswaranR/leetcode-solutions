class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xdiff = coordinates[1][0] - coordinates[0][0]
        ydiff = coordinates[1][1] - coordinates[0][1]

        for i in range(1, len(coordinates)):
            curr_xdiff = coordinates[i][0] - coordinates[0][0]
            curr_ydiff = coordinates[i][1] - coordinates[0][1]

            if ydiff * curr_xdiff != curr_ydiff * xdiff:
                return False
        
        return True
    

"""
If the third point is in same line as point 1 and 2:

(y2 - y1)   (y3 - y2)
--------- = ---------   ===>  (y2 - y1) * (x3 - x2) = (y3 - y2) * (x2 - x1)
(x2 - x1)   (x3 - x2)

"""