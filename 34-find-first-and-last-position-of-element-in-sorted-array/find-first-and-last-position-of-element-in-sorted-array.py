class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lists = []


        for i in range(len(nums)):
                if nums[i] == target:
                    lists.append(i)

        if len(lists) == 0:
                return [-1,-1]

        return [lists[0] , lists[-1]]
