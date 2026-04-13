class Solution:
    def smallestNumber(self, pattern: str) -> str:
        smaller = "9999999999"
        nums = [i for i in range(1,10)]
        def backtrack(taken,arr,i):
            nonlocal smaller
            if len(arr) == len(pattern)+1:
                digit = "".join(arr)
                if digit < smaller:
                    smaller = digit
                return
            
            for j in range(len(nums)):
                if pattern[i] == "I":
                    if arr:
                        if nums[j] <= int(arr[-1]):
                            continue
                else:
                    if arr:
                        if nums[j] >= int(arr[-1]):
                            continue
                if nums[j] in taken:
                    continue
                arr.append(str(nums[j]))
                taken.add(nums[j])
                backtrack(taken,arr,i+1)
                arr.pop()
                taken.remove(nums[j])
            
            return

        for n in nums:
            backtrack({n},[str(n)],0)
        return smaller