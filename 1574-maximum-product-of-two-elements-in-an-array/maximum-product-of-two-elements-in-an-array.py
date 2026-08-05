class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lists = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pro = (nums[i]-1) * (nums[j] - 1)
                lists.append(pro)
        return max(lists)
        