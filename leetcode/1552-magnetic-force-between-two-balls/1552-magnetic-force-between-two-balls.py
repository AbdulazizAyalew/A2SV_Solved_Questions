class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        low = 1
        high = max(position) - min(position) + 1
        position.sort()
        def can(mid):
            count_balls = 0
            pos = []
            for p in position:
                if pos:
                    if p - pos[-1] >= mid:
                        pos.append(p)
                        count_balls += 1
                else:
                    pos.append(p)
                    count_balls += 1
            return count_balls >= m

        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                low = mid + 1
            else:
                high = mid - 1
            
        
        return high
        