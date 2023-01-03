class Solution:
    def toLowerCase(self, s: str) -> str:
        arr = list(s)
        
        for i in range(len(arr)):
            if 65 <= ord(s[i]) <= 90:
                arr[i] = chr(ord(s[i]) + 32)
        
        return "".join(arr)


"""
Approach:

As the difference between the ascii value of a uppercase alphabet and it lowercase counterpart
is 32, we add 32 to the ascii value if the letter is uppercase.

"""