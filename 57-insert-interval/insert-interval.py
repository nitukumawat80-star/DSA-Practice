class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rev = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            rev.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0] , newInterval[0])
            newInterval[1] = max(intervals[i][1] , newInterval[1])
            i += 1

        rev.append(newInterval)

        while i < n:
            rev.append(intervals[i])
            i += 1

        return rev

        