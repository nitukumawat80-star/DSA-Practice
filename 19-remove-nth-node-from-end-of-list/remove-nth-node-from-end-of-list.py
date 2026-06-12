# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        Behind = Ahead = dummy

        for _ in range(n+1):
            Ahead = Ahead.next

        while Ahead:
            Ahead = Ahead.next
            Behind = Behind.next

        Behind.next = Behind.next.next

        return dummy.next
