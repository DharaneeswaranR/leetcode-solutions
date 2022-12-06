# Bucket sorting
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        n = len(s)
        bucket = [[] for _ in range(n + 1)]
        
        for c, f in freq.items():
            bucket[f].append(c)
        
        ans = ""
        for i in range(n, 0, -1):
            for c in bucket[i]:
                ans += c * i
                
        return ans

# Sort the dict elements based on frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        sort = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        s = ""
        for i in sort:
            s += i[0] * i[1]
            
        return s


"""
Solution:

Create a hashmap to store the frequency of occurance of chars and sort it in decending 
order using bucket sort.

"""