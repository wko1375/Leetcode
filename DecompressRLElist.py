class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        lst = []
        while i < len(nums):
            templst = [nums[i + 1]] * nums[i]
            lst += templst
            i += 2
        return lst
