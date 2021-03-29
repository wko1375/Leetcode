class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def palindromeHelper(s, start, end, flag):
            if start >= end:
                return True
            else:
                if s[start] == s[end]:
                    return palindromeHelper(s, start + 1, end - 1, flag)
                else:
                    if flag == True:
                        return False
                    elif s[start + 1] == s[end] or s[start] == s[end-1]:
                        return palindromeHelper(s, start + 1, end, True) or palindromeHelper(s, start, end - 1, True)
                    else:
                        return False
        if not s:
            return False
        return palindromeHelper(s, 0, len(s) - 1, False)
