class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res = len(words)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    res -= 1
                    break
        return res
                
                
