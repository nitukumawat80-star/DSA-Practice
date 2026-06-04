class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        
        i = 0
        l = len(s) - 1

        while l > i:
            s[i] , s[l] = s[l] , s[i]
            i += 1
            l -= 1
        return s