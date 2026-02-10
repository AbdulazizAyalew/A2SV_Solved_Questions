class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        Result = []
        for num in nums:
            str_num = str(num)
            new_arr = list(map(int,str_num))
            Result.extend(new_arr)

        
        return Result
        
