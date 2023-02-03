class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i, index = 0, {}

        for s in order:
            index[s] = i
            i += 1

        for i in range(len(words)-1):
            l1, l2 = len(words[i]), len(words[i+1])
            l = min(l1, l2)
            for j in range(l):
                if index[words[i][j]] < index[words[i+1][j]]:
                    break
                elif index[words[i][j]] == index[words[i+1][j]]:
                    if j == l - 1 and l1 > l2: # Condition for Example 3 testcase
                        return False
                else:
                    return False

        return True


"""
Map the new order using hashmap and then compare consecutive strings
"""