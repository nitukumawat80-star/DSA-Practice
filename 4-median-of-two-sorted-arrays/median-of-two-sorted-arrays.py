class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()

        re = len(num)
        mid = re // 2

        if re % 2 == 0:
            result =  (num[mid-1] + num[mid]) / 2.0
            return result
        else:
            return num[mid]