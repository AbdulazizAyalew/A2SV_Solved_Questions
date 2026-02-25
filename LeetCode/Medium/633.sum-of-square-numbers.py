class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxx = int(sqrt(c))
        minn = 0

        while minn <= maxx:
            summ = minn ** 2 + maxx ** 2
            if summ == c:
                return True
            elif summ > c:
                maxx -= 1
            else:
                minn += 1
        
        return False
