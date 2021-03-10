class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbols = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        lst = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                lst.append(s[i])
            else:
                if len(lst) == 0:
                    return False
                else:
                    if s[i] == symbols[lst[len(lst) - 1]]:
                        lst.pop(len(lst) - 1)
                    else:
                        return False
        return len(lst) == 0
                    
                
