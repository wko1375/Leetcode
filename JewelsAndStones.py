class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        ans = 0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if(stones[i] == jewels[j]):
                    ans += 1
                    continue
        return ans
