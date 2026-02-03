class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = str(x)
        L = 0
        r = len(number) - 1
        
        while L < r:
            if number[L] != number[r]:
                return False
            L += 1
            r -= 1
        return True
        
