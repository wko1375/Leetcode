class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decOne = int(a, 2)
        decTwo = int(b, 2)
        decAns = decOne + decTwo

        res = bin(decAns)
        return res[2:len(res)]
