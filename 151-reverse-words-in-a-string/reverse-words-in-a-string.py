class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.strip().split()

        rev = x[::-1]
        rev = " ".join(rev)
        return rev