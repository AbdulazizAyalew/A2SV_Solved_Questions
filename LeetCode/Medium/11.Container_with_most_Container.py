class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        R = len(height) - 1

        while l < R:
            areaa = (min(height[l],height[R]) * (R-l))
            if height[l] < height[R]:
                l += 1
            else:
                R -= 1
            max_area = max(areaa, max_area)

        return max_area