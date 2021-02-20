class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffled = [''] * len(s)
        ans = ''
        for i in range(len(indices)):
            shuffled[indices[i]] = s[i]
        for i in range (len(shuffled)):
            ans += shuffled[i]
        return ans
