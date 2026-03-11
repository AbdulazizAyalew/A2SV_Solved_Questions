class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                val = stack.pop()
                if val == 0:
                    score = 1
                else:
                    score = val * 2
                
                stack[-1] += score

        return stack[0]
        