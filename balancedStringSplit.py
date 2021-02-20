class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        rCount = 0
        lCount = 0
        while i < len(s):
            if s[i] == "R":
                rCount += 1
            elif s[i] == "L":
                lCount += 1
            if rCount == lCount:
                res += 1
                rCount = 0
                lCount = 0
            i += 1
        return res
                
