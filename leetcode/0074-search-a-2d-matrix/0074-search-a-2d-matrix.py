class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = -1


        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if row == -1:
            return False
        
        low = 0
        high = len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

