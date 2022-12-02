class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        arr = list(s)
        l, r = 0, len(s) - 1
        
        while l < r:
            while arr[l] not in v and l < r:
                l += 1
            while arr[r] not in v and l < r:
                r -= 1
                
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
        return ''.join(arr)