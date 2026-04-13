class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if not s:
            return [""]

        queue = deque([s])
        visited = {s}
        found = False
        result = []

        while queue:
            level_size = len(queue)
            level_valid_strings = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if isValid(curr):
                    level_valid_strings.append(curr)
                    found = True
                
                if not found:
                    for i in range(len(curr)):
                        if curr[i] not in "()":
                            continue
                        
                        next_s = curr[:i] + curr[i+1:]
                        if next_s not in visited:
                            visited.add(next_s)
                            queue.append(next_s)
            

            if found:
                return level_valid_strings
        
        return [""]