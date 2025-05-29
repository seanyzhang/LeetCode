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
        trav = head
        while trav:
            for i in range(m-1):
                if not trav: return head
                trav = trav.next

            if not trav: return head

            dummy = trav.next
            for i in range(n):
                if not dummy: break
                dummy = dummy.next
            
            trav.next = dummy
            trav = trav.next

        return head
