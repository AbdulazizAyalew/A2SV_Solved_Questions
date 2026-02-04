from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        count_a = Counter(a)
        count_b = Counter(b)
        
        return (count_a == count_b) 
