class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0,10:0,20:0}

        for bill in bills:
            changes[bill] += 1
            if bill == 5:
                continue
            elif bill == 10:
                if changes[5] > 0:
                    changes[5] -= 1
                else:
                    return False
            else:
                if changes[5] > 0:
                    if changes[10] > 0:
                        changes[10] -= 1
                        changes[5] -= 1
                    else:
                        if changes[5] > 2:
                            changes[5] -= 3
                        else:
                            return False
                else:
                    return False

        return True 
        