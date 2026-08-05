class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mins = min(nums)
        maxs = max(nums)
        result = []
        for i in range(mins , maxs):
            if i in nums:
                continue
            else:
                result.append(i)
        return result
                
        