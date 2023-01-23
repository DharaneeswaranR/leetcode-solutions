# My initial approach
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        votes = [0] * (n + 1)
        voted = [0] * (n + 1)
        
        for t in trust:
            votes[t[1]] += 1
            voted[t[0]] += 1

        for i in range(1, n+1):
            if votes[i] == n - 1 and voted[i] == 0:
                return i
                
        return -1

# In-degree - Out-degree
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counts = [0] * (n + 1)
        
        for t in trust:
            counts[t[1]] += 1
            counts[t[0]] -= 1

        for i in range(1, n+1):
            if counts[i] == n - 1:
                return i
                
        return -1


"""
Approach: 

1. Create two arrays of length n + 1 to keep track of count of people's votes and no of 
   people they have voted. A judge would have n - 1 vote and he would have voted 0

2. In-degree - Out-degree = n - 1
   Considering the trust pair as directed edges of graph. 

"""