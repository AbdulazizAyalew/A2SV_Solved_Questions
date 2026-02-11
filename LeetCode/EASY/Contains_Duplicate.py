class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
            Appearance = set()
            for num in nums:
                if num in Appearance:
                    return True
                else:
                    Appearance.add(num)
            else:
                return False
