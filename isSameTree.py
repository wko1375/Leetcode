# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif q == None and p != None:
            return False
        elif p.val == q.val:
            curr = True
            left = self.isSameTree(p.left, q.left) 
            right = self.isSameTree(p.right, q.right)
            return curr and right and left
        else:
            return False
        
        
        
