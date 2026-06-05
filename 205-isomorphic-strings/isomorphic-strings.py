class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapst , mapts = {} , {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in mapst:
                if mapst[c1] != c2:
                    return False
            else:
                mapst[c1] = c2
            

            if c2 in mapts:
                if mapts[c2] != c1:
                    return False
            else:
                mapts[c2] = c1
        return True