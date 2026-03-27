class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 0:
            i = n // 2
            return ((self.myPow(5,i)) * (self.myPow(4,i))) % (10 ** 9 + 7)
        else:
            i = n // 2
            j = i + 1
            return ((self.myPow(5,j)) * (self.myPow(4,i))) % (10 ** 9 + 7)
        
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half = self.myPow(x,n//2)

        if n % 2 != 0:
            return( x * half * half )% (10 ** 9 + 7)
        else:
            return (half * half) % (10 ** 9 + 7)