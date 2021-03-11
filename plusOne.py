class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            if digits[0] == 9:
                return [1,0]
            digits[0] += 1
            return digits
        else:
            s = map(str,digits)
            s = "".join(s)
            s = int(s)
            s += 1
            s = str(s)
            res = []
            for i in range(len(s)):
                res.append(s[i])
            return res
                
            
