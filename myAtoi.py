class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            res = ""
            index = 0
            
            #Remove Whitespace
            while s[index] == " ":
                if index == len(s):
                    return 0
                index += 1
                if index == len(s):
                    return 0
            #Check for sign - start is = first index that there is no whitespace
            negative = 1
            
            if s[index] == "-" or s[index] == "+":
                if s[index] == "-":
                    negative = -1
                index += 1
            if index == len(s):
                return 0
            if not(48 <= ord(s[index]) <= 57):
                return 0
            
            #Loop through rest of string and add to res if a number
            for i in range(index, len(s)):
                if (48 <= ord(s[i]) <= 57):
                    res += s[i]
                    continue
                else:
                    break
            newRes = int(res) * negative
            if newRes >= pow(2, 31):
                newRes = pow(2, 31) - 1
            if newRes < -pow(2, 31):
                newRes = -pow(2, 31)

            return newRes 
