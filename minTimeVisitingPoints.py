import math
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        seconds = 0
        for i in range( len(points) - 1):
            start = points[i]
            end = points[i + 1]

            '''if fp[0] == sp[0] and fp[1] == sp1[1]:'''
            
           
            while abs(end[0] - start[0]) >= 1 and abs(end[1] - start[1]) >= 1:
                x1 = start[0]
                y1 = start[1]
                x2 = end[0]
                y2 = end[1]
                if x1 < x2 and y1 < y2:
                    start[0] += 1
                    start[1] += 1
                elif x1 < x2 and y1 > y2:
                    start[0] += 1
                    start[1] -= 1
                elif x1 > x2 and y1 > y2:
                    start[0] -= 1
                    start[1] -= 1
                else:
                    start[0] -= 1
                    start[1] += 1
                seconds += 1
            if start == end:
                continue
            elif start[0] == end[0]:
                seconds += abs(start[1] - end[1])
            else:
                seconds += abs(start[0] - end[0])
            
        return seconds
                
            
                    
            
                
