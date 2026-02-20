class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        print(points)

        count = 1
        lower = points[0][0]
        upper = points[0][1]

        for i in range(1,len(points)):
            if points[i][0] <= upper:
                lower = points[i][0]
                upper = min(points[i][1],upper)
            else:
                count += 1
                lower = points[i][0]
                upper = points[i][1]
        
        return count





















































