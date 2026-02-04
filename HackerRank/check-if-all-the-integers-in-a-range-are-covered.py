class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for i in range(left,right + 1):
            for j in range(len(ranges)):
                if i >= ranges[j][0] and i <= ranges[j][1]:
                    break
            else:
                return False
        else:
            return True
