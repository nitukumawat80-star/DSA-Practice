# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        num = []
        curr = head

        while curr:
            num.append(curr.val)
            curr = curr.next

        l , r = 0 , len(num) -1

        while l < r:
            if num[l] != num[r]:
                return False
            
            l += 1
            r -= 1

        return True
