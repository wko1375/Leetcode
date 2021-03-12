# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        elif len(nums) == 0:
            return None
        else:
            mid = len(nums)/2
            leftNode = self.sortedArrayToBST(nums[0:mid])
            rightNode = self.sortedArrayToBST(nums[mid+1: len(nums)])
            r = TreeNode(nums[mid], leftNode , rightNode)
            return r
