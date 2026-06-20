class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r = 0,x
        re = 0
        while l <= r:
            m = (l + r) // 2
            if m*m > x:
                r = m - 1
            elif m*m < x:
                l = m + 1
                re = m
            else:
                return m
        return re