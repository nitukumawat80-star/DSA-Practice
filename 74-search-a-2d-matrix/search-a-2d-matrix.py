class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l , r = 0 , t - 1
        while r >= l:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n
            num = matrix[i][j]

            if target == num:
                return True

            elif num < target:
                l = mid + 1

            else:
                r = mid - 1

        return False
        