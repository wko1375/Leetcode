class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = 0
        ans = 0
        for elem in gain:
            res += elem
            if res > ans:
                ans = res
        return ans
