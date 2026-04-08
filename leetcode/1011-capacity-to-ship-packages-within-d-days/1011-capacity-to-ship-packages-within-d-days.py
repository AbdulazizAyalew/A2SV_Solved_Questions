class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def can(mid):
            Days_taken = [0]
            for i in range(len(weights)):
                if Days_taken[-1] + weights[i] <= mid:
                    Days_taken[-1] += weights[i]
                else:
                    Days_taken.append(weights[i])
            
            return len(Days_taken) <= days

        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
