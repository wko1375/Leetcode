class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        for i in range(len(s)):
            n = s[i]
            if i == len(s) - 1:
                res += letters[n]
                return res
            elif(n == "I"):
                if(s[i+1] == "V" or s[i+1] == "X"):
                    res -= 1
                else:
                    res += 1
                continue
            elif(n == "X"):
                if(s[i+1] == "L" or s[i+1] == "C"):
                    res -= 10
                else:
                    res += 10
                continue
            elif(n == "C"):
                if(s[i+1] == "D" or s[i+1] == "M"):
                    res -= 100
                else:
                    res += 100
                continue
            res += letters[n]
        return res
