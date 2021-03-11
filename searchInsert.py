class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
            elif nums[i] >= target:
                return i
            elif nums[i] <= target and i == len(nums) - 1:
                return len(nums)
            else:
                continue
        return -1
         
