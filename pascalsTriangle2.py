class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def generate(numRows):
            if numRows == 1:
                return [[1]]
            elif numRows == 0:
                return [[]]
            elif numRows == 2:
                return [[1],[1,1]]
            else:
                res = []
                lst = [1]
                nextRow = generate(numRows - 1)
                for i in range(len(nextRow[-1]) - 1):
                    lst.append(nextRow[-1][i] + nextRow[-1][i+1])
                lst.append(1)
                nextRow.append(lst)
            return nextRow
        lst = generate(rowIndex + 1)
        return lst[rowIndex]
