class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(haystack)
        b = len(needle)

        for i in range(a-b+1):
            if haystack[i:b+i] == needle:
                return i
        return -1
        