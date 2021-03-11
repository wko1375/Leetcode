class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i], nums[len(nums)-1] = nums[len(nums)-1], nums[i]
                nums.pop()
                continue
            else:
                i += 1
                continue
        return len(nums)
                
