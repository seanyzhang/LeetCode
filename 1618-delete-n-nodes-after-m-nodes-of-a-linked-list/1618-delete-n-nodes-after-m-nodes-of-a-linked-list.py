# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: Optional[ListNode]
        :type m: int
        :type n: int
        :rtype: Optional[ListNode]
        """
        slow, fast = head, head

        while fast:
            M = m
            N = n
            while fast and M > 0:
                slow = fast
                fast = fast.next
                M -= 1

            while fast and N > 0:
                fast = fast.next
                N -= 1
            
            slow.next = fast

        return head

