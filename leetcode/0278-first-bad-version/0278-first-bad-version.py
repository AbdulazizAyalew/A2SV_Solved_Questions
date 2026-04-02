# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        minn = 1
        maxx = n
        if n == 1:
            return 1
        while minn < maxx:
            mid = (maxx + minn) // 2
            if isBadVersion(mid) == False:
                if isBadVersion(mid+1) == True:
                    return mid + 1
                else:
                    minn = mid
            else:
                if isBadVersion(mid-1) == False:
                    return mid
                else:
                    maxx = mid
        
