from collections import defaultdict
s = input()

stack = []
for i, b in enumerate(s):
    if b == ')':
        if stack and s[stack[-1]] == '(':
            stack.pop()
            continue
    stack.append(i)

stack.append(len(s))

mapp = defaultdict(int)

mx = stack[0]
mapp[mx] += 1
for i in range(1, len(stack)):
    sep = (stack[i] - stack[i-1]) - 1
    mx = max(mx, sep)
    mapp[sep] += 1

mapp[0] = 1

print(mx, mapp[mx])