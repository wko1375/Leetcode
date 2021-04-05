class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.split()
        res = ""
        i = len(x)- 1
        while i > 0:
            res += x[i]
            res += " "
            i -= 1
        res += x[0]
        return res
