class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -= 1
        return boats

"""
Approach: Greedy 

- As only two people can be on the boat at a time, we need to find the smallest weight person and the largest weight person
  to maximize the space utilization and minimize the number of boats needed.
- If the boat can fit both the small and large weigth person we increment left and decrement right.
- Else we decrement right to fit large weight person.

"""