class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newlist = ""
        for ch in s:
            if ch.isalnum():
                newlist = newlist + ch.lower()


        return newlist == newlist[::-1]       
        