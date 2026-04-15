class Solution:
    def splitString(self, s: str) -> bool:
    
        for i in range(1, len(s)):
            val = int(s[:i])
            if self.backtrack(s, i, val):
                return True
        return False

    def backtrack(self, s, index, prev_val):

        if index == len(s):
            return True
        

        for j in range(index + 1, len(s) + 1):
            current_val = int(s[index:j])

            if current_val == prev_val - 1:
                if self.backtrack(s, j, current_val):
                    return True
            
        
            if current_val >= prev_val:
                break
                
        return False