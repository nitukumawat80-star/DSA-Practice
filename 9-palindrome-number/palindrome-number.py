class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        org = x
        sum = 0
        while x > 0:
            digit = x % 10
            sum = sum * 10 + digit
            x //= 10
        if sum == org :
            return True
        else:
            return False
        