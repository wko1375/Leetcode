# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def maxDepthOfTree(root):
            
            if root == None:
                return 0
            elif root.left == None and root.right == None:
                return 1
            elif root.left != None and root.right != None:
                leftDepth = maxDepthOfTree(root.left)
                rightDepth = maxDepthOfTree(root.right)
                return 1 + max(leftDepth, rightDepth)
            elif root.left == None:
                return 1 + maxDepthOfTree(root.right)
            elif root.right == None:
                return 1 + maxDepthOfTree(root.left)
            else:
                return 1 
        
        if not root:
            return True
        elif root.left == None and root.right == None:
            return True
        else:
            leftDepth = maxDepthOfTree(root.left)
            rightDepth = maxDepthOfTree(root.right)
            diff = abs(leftDepth - rightDepth)
            return diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
