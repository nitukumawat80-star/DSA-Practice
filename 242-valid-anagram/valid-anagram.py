class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lists1 = list(s)
        lists2 = list(t)
        lists1.sort()
        lists2.sort()
        if lists1 == lists2:
            return True
        else:
            return False