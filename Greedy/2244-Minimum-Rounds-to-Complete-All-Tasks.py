class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = {}
        minrounds = 0

        for task in tasks:
            if task in counts:
                counts[task] += 1
            else:
                counts[task] = 1

        for count in counts.values():
            if count == 1:
                return -1
            elif count % 3 == 0:
                minrounds += count // 3
            else:
                minrounds += (count + 2) // 3

        return minrounds


"""
Approach: Counting and Greedy

Use hash map to count the tasks of same type, to get minimum rounds, the counts should be
grouped by 3 and the remainder are grouped by 2.

Ex:

1. count is 1 - cant be grouped in 3 or 2 hence return -1
2. count is divisible by 3 - add result after dividing by 3
3. count not divisible by 3
   formula = (count + 2) / 3

   count = 2
   (count + 2) / 3 = 4 / 3 = 1 (grouped - 2)
   count = 5
   7 / 2 = 2 (grouped - 3, 2)
   count = 7
   9 / 3 = 3 (grouped - 3, 2, 2)


"""