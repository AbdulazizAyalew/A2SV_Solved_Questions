class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        no_operation = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles != 0:
                no_operation += 1
                target = target // 2
                maxDoubles -= 1
            else:
                if maxDoubles == 0:
                    no_operation += (target - 1)
                    break
                no_operation += 1
                target -= 1
        
        return no_operation