class Solution(object):
    def toLowerCase(self, str):
        res = ""
        for i in range(len(str)):
            t = ord(str[i])
            if 65 <= t <= 90:
                t += 32
            res += chr(t)
        return res
