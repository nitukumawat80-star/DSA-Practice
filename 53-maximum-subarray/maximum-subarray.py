class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxs = nums[0]
        sums = 0
        for i in (nums):
            if sums < 0:
                sums = 0
            sums += i
            maxs = max(maxs,sums)
        return maxs
       

        