class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        stack = []
        nums = {"0","1","2","3","4","5","6","7","8","9"}


        for i in range(len(s)):
            if  s[i] == "]":
                st = []
                while stack[-1] not in nums:
                    val = stack.pop()
                    if val != "[":
                        st.append(val)
                num = []
                while stack and stack[-1] in nums:
                    num.append(stack.pop())
                num.reverse()

                k = int("".join(num))
                new_s = []
                st.reverse()

                for i in range(k):
                    new_s.append("".join(st))

                if stack:
                    stack.append("".join(new_s))
                else:
                    result.append("".join(new_s))        
            else:
                stack.append(s[i])

    
        result.extend(stack)

        return "".join(result)
        