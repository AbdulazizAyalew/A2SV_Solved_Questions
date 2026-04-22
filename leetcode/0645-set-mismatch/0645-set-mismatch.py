class Solution:
    def findErrorNums(self, nums):
        maxx = len(nums)
        Nums_set = set()
        check_set = set()
        ans = []
        for n in range(1, maxx + 1):
            Nums_set.add(n)
        
        for n in nums:
            if n in check_set:
                ans.append(n)
            check_set.add(n)

        for n in Nums_set:
            if n not in check_set:
                ans.append(n)
        
        return ans