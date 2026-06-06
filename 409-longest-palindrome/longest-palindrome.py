class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        rev = 0

        for ch in s:
            if ch in seen:
                seen.remove(ch)
                rev += 2

            else:
                seen.add(ch)

        if seen:
            rev += 1

        return rev       