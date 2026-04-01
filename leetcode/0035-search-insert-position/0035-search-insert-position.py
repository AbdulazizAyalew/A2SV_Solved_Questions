class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        indx = -1
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                indx = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        if indx != -1:
            return indx
        else:
            if nums[mid] > target:
                return mid
            else:
                return mid + 1