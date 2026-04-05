class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        low = 0
        high = max(
            abs(max(houses) - min(heaters)),
            abs(min(houses) - max(heaters))
        )        
        heaters.sort()

        def can(rad):
            for h in houses:
                left = 0
                right = len(heaters) - 1
                found = False

                while left <= right:
                    mid = (left + right) // 2

                    if heaters[mid] < h - rad:
                        left = mid + 1
                    elif heaters[mid] > h + rad:
                        right = mid - 1
                    else:
                        found = True
                        break

                if not found:
                    return False

            return True
        
        while low <= high:
            mid  = (low + high) // 2
            if can(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
        
            