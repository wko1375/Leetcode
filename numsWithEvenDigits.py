class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for elem in nums:
            s = str(elem)
            if len(s) % 2 == 0:
                count += 1
        return count
