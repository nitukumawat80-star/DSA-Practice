class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        sign = 1
        if x < 0:
         x = -x
         sign = -1
        while x>0:
          last = x % 10
          rev = rev * 10 + last
          x = x//10
        rev *= sign
        if rev < -2**31 or rev > 2**31:
            return 0
        return rev