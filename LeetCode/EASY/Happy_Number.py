class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited_square = set()
        while n != 1:
            if n in visited_square:
                break
            visited_square.add(n)
            n = sum(int(num) ** 2 for num in str(n))
        else:
            return True
        
        return False
               

            
