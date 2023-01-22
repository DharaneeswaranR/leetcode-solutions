class Solution:
    # Convert HH:MM string to minutes integer
    def toMinutes(self, time) -> int:
        hours, minutes = [int(x) for x in time.split(":")]
        return hours * 60 + minutes

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = self.toMinutes(event1[0]), self.toMinutes(event1[1]) 
        start2, end2 = self.toMinutes(event2[0]), self.toMinutes(event2[1])

        if start1 < start2:
            return start2 <= end1
        else:
            return start1 <= end2 
        