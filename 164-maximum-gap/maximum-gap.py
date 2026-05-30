class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        
        nums.sort()
        maxs = 0
        for i in range(1,len(nums)):
            maxs =  max(maxs,nums[i] - nums[i-1])
        return maxs
        