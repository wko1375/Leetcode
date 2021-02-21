# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if(low <= root.val and root.val <= high):
            res = root.val
        else:
            res = 0
            
        if(root.left != None):
            res += self.rangeSumBST(root.left, low, high)
        if(root.right != None):
            res += self.rangeSumBST(root.right, low, high)
        return res
 
            
        
       
