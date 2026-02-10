class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = 0
        for n in nums:
            if n % 2 == 0:
                sum_even += n
        
        Result = []

        for query in queries:
            if nums[query[1]] % 2 == 0:
                summ = nums[query[1]] + query[0]
                if summ % 2 == 0:
                    sum_even += query[0]
                else:
                    sum_even -= nums[query[1]]
                nums[query[1]] = summ
                Result.append(sum_even)
            else:
                summ = nums[query[1]] + query[0]
                if summ % 2 == 0:
                    sum_even += summ
                nums[query[1]] = summ
                Result.append(sum_even)
        
        return Result
