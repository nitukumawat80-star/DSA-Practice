class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            max1 = stones[-1]
            max2 = stones[-2]
            stones.pop()
            stones.pop()
            if max1 != max2:
                stones.append(max1-max2)
           
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        