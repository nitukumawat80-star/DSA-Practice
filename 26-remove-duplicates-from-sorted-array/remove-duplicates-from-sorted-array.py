class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lists = []
        for i in range(len(nums)):
            if nums[i] not in lists:
                lists.append(nums[i])

        for j in range(len(lists)):
            nums[j] = lists[j]
        
        return len(lists)