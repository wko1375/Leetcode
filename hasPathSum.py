# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if root == None:
            return False
        elif root.left == None and root.right == None:
            return (targetSum - root.val == 0)
        elif root.left == None:
            return self.hasPathSum(root.right, targetSum - root.val)
        elif root.right == None:
            return self.hasPathSum(root.left, targetSum - root.val)
        else:
            n = targetSum - root.val
            return self.hasPathSum(root.left, n) or self.hasPathSum(root.right, n)
            
            
