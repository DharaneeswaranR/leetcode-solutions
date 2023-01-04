class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletions = 0
        strlen = len(strs[0])

        for i in range(strlen):
            for j in range(0, len(strs)-1):
                if not strs[j][i] <= strs[j+1][i]:
                    deletions += 1
                    break
        
        return deletions

