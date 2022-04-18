class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            
            hashset.add(num)
            
        return False


"""
Approach:

As this problem requires searching if an value is present, we can use hashset (O(1) for seaching) 
to store the values present in the array while simultaneously checking if the value is already 
present in the array.

Time complexity - O(n)

"""
        