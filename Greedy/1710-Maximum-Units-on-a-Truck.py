class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_units = 0

        for boxes, units in boxTypes:
            if boxes <= truckSize:
                max_units += (boxes * units)
                truckSize -= boxes
            else:
                max_units += (truckSize * units)
                break

        return max_units


"""
Approach: Greedy

Sort by units the apply greedy algorithm

"""