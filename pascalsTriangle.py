class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 0:
            return [[]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            res = []
            lst = [1]
            nextRow = self.generate(numRows - 1)
            for i in range(len(nextRow[-1]) - 1):
                lst.append(nextRow[-1][i] + nextRow[-1][i+1])
            lst.append(1)
            nextRow.append(lst)
        return nextRow
                
            
        
