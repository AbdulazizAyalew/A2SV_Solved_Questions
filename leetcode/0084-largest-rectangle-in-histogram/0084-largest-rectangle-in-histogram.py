class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_valids = [-1] * len(heights)
        valids = []

        for i in range(len(heights)) :
            while valids and valids[-1][0] >= heights[i] :
                valids.pop()
            if valids :
                left_valids[i] = valids[-1][1]    
            valids.append([heights[i], i])

            
        right_valids = [len(heights)] * len(heights)
        valids = []
        for i in range(len(heights) - 1, -1, -1 ):
            while valids and valids[-1][0] >= heights[i] :
                valids.pop()
            if valids :
                right_valids[i] = valids[-1][1]    
            valids.append([heights[i], i])
        ans = 0    
        for i in range(len(right_valids)) :
            right_valids[i] = right_valids[i] - left_valids[i] - 1
            ans = max(ans, right_valids[i] * heights[i])
        return ans        


