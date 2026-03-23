class Solution:
    def minOperations(self, nums: List[int]) -> int:
        que = deque()
        min_op = 0
        i = 0
        while i < len(nums):

            # To Add 
            while len(que) < 3 and i < len(nums):
                if len(que) == 0:
                    if nums[i] == 1:
                        i += 1
                        continue
                que.append(nums[i])
                i += 1
            
            if len(que) != 3:
                break
            min_op += 1
            for j in range(3):
                que[j] = 1 if que[j] == 0 else 0
            
            while len(que) != 0:
                if que[0] == 1:
                    que.popleft()
                else:
                    break
        
        
        if len(que) != 0:
            return -1
        else:
            return min_op