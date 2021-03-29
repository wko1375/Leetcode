class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isNumOrLetter(s):
            return s.isdigit() or s.isalpha()
        
        start = 0
        end = len(s) - 1
        s1 = s.lower()
        while start < end:
            l1 = s1[start]
            l2 = s1[end]
            if isNumOrLetter(l1):
                if isNumOrLetter(l2):
                    if l1 == l2:
                        start += 1
                        end -= 1
                        continue
                    else:
                        return False
                else:
                    end -= 1
                    continue
            elif isNumOrLetter(l2):
                start += 1
                continue
            else:
                start += 1
                end -= 1
                continue
        return True
        
        
        
                
                
        
        
        
