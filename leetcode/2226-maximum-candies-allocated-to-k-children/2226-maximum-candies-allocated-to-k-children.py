class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = max(candies)

        def can(mid):
            count = 0
            for i in range(len(candies)):
                count += (candies[i] // mid)

            return count >= k
        
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high
        