class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = deque([])
        res = []

        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num) 

        for num in nums1:
            res.append(hashmap.get(num, -1))

        return res


"""
Approach: Monotomic stack

Similar to 739-Daily-Temperatures

"""