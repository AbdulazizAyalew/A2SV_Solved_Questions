#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        counter_a = Counter(a)
        counter_b = Counter(b)
        
        for num in counter_b:
            if num not in counter_a:
                return False
            else:
                if counter_a[num] < counter_b[num]:
                    return False
        else:
            return True
    
    
    
    
