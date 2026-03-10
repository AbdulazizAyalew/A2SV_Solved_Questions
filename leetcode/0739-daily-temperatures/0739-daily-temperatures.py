class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indx_map = {i:0 for i in range(len(temperatures))}

        res = []
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures [i] > temperatures[stack[-1]]:
                    indx_map[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)

        for j in range(len(temperatures)):
            res.append(indx_map[j])

        return res