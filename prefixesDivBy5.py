class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """

        res = []
        if not A:
            return res
        bNum = ""
        for elem in A:
            bNum += str(elem)
            converted = int(bNum, base=2)
            if converted % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
            
            
