class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == " ":
            return 0
        elif len(s) == 1:
            return 1
        else:
            lst = s.split()
            if lst:
                return len(lst[len(lst) - 1])
            else:
                return 0
