class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxs  = 0
        nums.sort()
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            maxs = max(maxs, diff)
        return maxs
        