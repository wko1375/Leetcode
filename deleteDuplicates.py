# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p != None:
            if p.next == None:
                return head
            elif p.next.val == p.val:
                p.next = p.next.next
                continue
            else:
                p = p.next
        return head
