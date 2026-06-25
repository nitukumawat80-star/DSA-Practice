class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        mins = 0
        right = len(height) - 1

        while left < right:
            w = right - left
            h = min(height[left] , height[right])
            area = w * h
            mins = max(mins , area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mins  