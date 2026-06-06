class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.strip().split()

        i = 0
        j = len(x) - 1

        while j > i:
            x[i] , x[j] = x[j] , x[i]
            i += 1
            j -= 1

        rev = " ".join(x)
        return rev

       