class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}
        for i in range(len(nums) - k + 1):
            window = set(nums[i:i+k])

            for j in window:
                count[j] = count.get(j,0) + 1

        ans = -1

        for num , fre in count.items():
            if fre == 1:
                ans = max(ans , num)

        return ans
        
        