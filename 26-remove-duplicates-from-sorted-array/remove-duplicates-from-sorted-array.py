class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        for n in range(1,len(nums)):
            if nums[n] != nums[n-1]:
                nums[l] = nums[n]
                l += 1
        return l
