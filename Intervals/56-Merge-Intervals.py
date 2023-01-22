class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:   # overlaps - merge it
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start, end = intervals[i]

        res.append([start, end])
        return res


"""
Approach: Overlapping Intervals

Whenever an interval overlaps with current interval, merge it by finding new end using max()
else if it doesnt overlap add it to result and assign new start and end

"""