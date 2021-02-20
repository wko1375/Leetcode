class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = list(str(n))
        mult = 1
        add = 0
        for i in range(len(lst)):
            lst[i] = int(lst[i])
            mult *= lst[i]
            add += lst[i]
        return mult - add
