# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def createLinkedList(lst, index):
            if index == len(lst):
                return None
            else:
                n = ListNode(lst[index])
                n.next = createLinkedList(lst, index + 1)
            return n
        sortedLst = []
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            p1, p2 = l1, l2

            while p1 != None or p2 != None:
                if p1 == None and p2 != None:
                    sortedLst.append(p2.val)
                    p2 = p2.next
                    continue
                elif p2 == None and p1 != None:
                    sortedLst.append(p1.val)
                    p1 = p1.next
                    continue
                else:
                    if p1.val >= p2.val:
                        sortedLst.append(p2.val)
                        p2 = p2.next
                        continue
                    elif p2.val > p1.val:
                        sortedLst.append(p1.val)
                        p1 = p1.next
                        continue
                    continue
            return createLinkedList(sortedLst, 0)
        
                
                    
            
                
        
