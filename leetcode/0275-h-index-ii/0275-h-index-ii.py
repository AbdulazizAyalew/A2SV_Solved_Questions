class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = max(citations)

        def can(mid):
            i = 0
            while i < len(citations):
                if citations[i] >= mid:
                    break
                i += 1
            no = len(citations) - i

            return no >= mid

        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
