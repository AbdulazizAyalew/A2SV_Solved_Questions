class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mid = float('-inf')
        for i in reversed(nums):
            if i < mid:
                return True
            while stack and i > stack[-1]:
                mid = stack.pop()

            stack.append(i)

        return False