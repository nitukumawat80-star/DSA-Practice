class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        a = list(s)
        l = len(a) - 1

        while l > 0 and a[l] == " ":
            l -= 1
        while l >= 0 and a[l] != " ":
            l -= 1
            count += 1
        return count