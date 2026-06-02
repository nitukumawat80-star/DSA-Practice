class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = float('inf')
        maximum = 0

        for price in prices:
            if price < minimum:
                minimum = price
            profit = price - minimum
            maximum = max(maximum , profit)
        return maximum
        