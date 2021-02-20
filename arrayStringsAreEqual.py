class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        first = ""
        second = ""
        for elem in word1:
            first += elem
        for elem in word2:
            second += elem
        if(first == second):
            return True
        else:
            return False
