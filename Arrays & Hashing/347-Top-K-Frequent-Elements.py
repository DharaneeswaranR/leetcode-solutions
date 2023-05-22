# Sorting - O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) 

        for n in nums:
            freq[n] += 1

        freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = []

        for i in range(k):
            res.append(freq_sorted[i][0])
            
        return res


# Heap - O(nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        return heapq.nlargest(k, freq.keys(), lambda x: freq[x])
    

# Bucket Sort - O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freq[n] += 1
        
        for key, val in freq.items():
            bucket[val].append(key)

        res = []

        for i in range(-1, -len(bucket), -1):
            if bucket[i]:
                for n in bucket[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        

        