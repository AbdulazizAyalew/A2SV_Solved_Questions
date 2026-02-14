class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed_count = Counter(changed)
        
        Result = []
        if 0 in changed_count:
            if changed_count[0] % 2 == 0:
                count_0 = changed_count[0] // 2
            else:
                return []
        changed.sort()
              
        for num in changed:
            double = num * 2
            if num != 0 and changed_count[num] > 0 and double in changed_count and changed_count[double] > 0:
                changed_count[double] -= 1
                changed_count[num] -= 1
                Result.append(num)
            elif num == 0 and changed_count[num] > count_0 and count_0 != 0:
                Result.append(num)
                changed_count[num] -= 1

        if Result == []:
            return []
        else:
            if len(Result) * 2 != len(changed):
                return []
            else:
                return Result
