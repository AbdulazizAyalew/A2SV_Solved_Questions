class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        new_arr = sorted(nums, reverse=True)
        Result = ""

        for i in range(len(new_arr)):
            for j in range(i + 1, len(new_arr)):
                num1 = str(new_arr[i])
                num2 = str(new_arr[j])
                if num1 + num2 < num2 + num1:
                    new_arr[i], new_arr[j] = new_arr[j], new_arr[i]

        for i in range(len(new_arr)):
            Result += str(new_arr[i])

        if Result[0] == '0':
            return '0'

        return Result


