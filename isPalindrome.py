class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        toString = str(x)
        revString = toString[::-1]
        return toString == revString
