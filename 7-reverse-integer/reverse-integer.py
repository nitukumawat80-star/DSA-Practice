class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sing = 1
        rev = 0
        if x < 0:
            x = -x
            sing  = -1

        while x > 0:
            last = x % 10
            rev = rev * 10 + last
            x //= 10

        rev = rev * sing
        if rev < -2**31 or rev > 2**31:
            return 0

        return rev  