class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        
        for n in nums:
            dic[n] = dic.get(n , 0) + 1

        for i , j in dic.items():
            if dic[i] > 1:
                return i
              
       