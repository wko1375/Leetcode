class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        m = min(len(word1), len(word2))
        for i in range(m):
            res += word1[i] + word2[i]
        if len(word2) > len(word1):
            res += word2[m:len(word2)]
        elif len(word1) > len(word2):
            res += word1[m:len(word1)]
        else:
            return res
        return res
        
