class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        lst = []
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
                lst.append(count)
            elif s[i] == ")":
                count -= 1
                lst.append(count)
            else:
                continue
        m = 0
        for elem in lst:
            m = max(elem, m)
        return m
