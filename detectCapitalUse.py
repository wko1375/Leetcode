class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        elif word.islower():
            return True
        else:
            ans = True
            if word[0].isupper() and word[1:len(word)].islower():
                return True
            else:
                return False
