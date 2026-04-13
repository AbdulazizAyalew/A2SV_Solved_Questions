class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break   
            for j in range(1, n - i):
                if num[i] == '0' and j > 1:
                    break
                
                num1 = int(num[:i])
                num2 = int(num[i:i+j])
                
                if self.can_complete(num1, num2, i + j, num):
                    return True
                    
        return False

    def can_complete(self, n1, n2, start_idx, num):
        if start_idx == len(num):
            return True
        
        target_sum = n1 + n2
        target_str = str(target_sum)
        

        if not num.startswith(target_str, start_idx):
            return False
        
        return self.can_complete(n2, target_sum, start_idx + len(target_str), num)