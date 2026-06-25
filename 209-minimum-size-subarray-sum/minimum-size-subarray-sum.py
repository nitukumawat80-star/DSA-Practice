class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        sum = 0
        min_index = float('inf')
        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_index = min(min_index, right-left+1)
                sum -= nums[left]
                left += 1

        if min_index == float('inf'):
            return 0

        else:
            return min_index
        