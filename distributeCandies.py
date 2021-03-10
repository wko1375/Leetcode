class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        if not candyType:
            return 0
        elif len(candyType) == 2:
            return 1
        else:
            res = list(set(candyType))
        n = (len(candyType)/2)
        if n >= len(res):
            return len(res)
        else:
            return n
