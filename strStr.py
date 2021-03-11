class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        else:
            length = len(needle)
            for i in range(len(haystack)):

                if haystack[i:i+length] == needle:
                    return i
        return -1

        
