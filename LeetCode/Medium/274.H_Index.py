class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 1
        max_h = 0
        maxx = max(citations)
        while h <= maxx:
            count = 0
            for i in range(len(citations)):
                if citations[i] >= h:
                    count += 1
            if count >= h:
                max_h = max(h,max_h)
            else:
                break
            h += 1
        return max_h
            

                
