class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        result = []
        for j in range(k):
            if que:
                if nums[que[-1]] > nums[j]:
                    que.append(j)
                else:
                    while que and nums[que[-1]] < nums[j]:
                        que.pop()
                    que.append(j)
            else:
                que.append(j)
        result.append(nums[que[0]])

        
        
        for i in range(k,len(nums)):
            if que:
                if nums[que[-1]] > nums[i]:
                    que.append(i)
                else:
                    while que and nums[que[-1]] < nums[i]:
                        que.pop()
                    que.append(i)
            else:
                que.append(i)
            
            while que and i-que[0] >= k:
                que.popleft()
            
            result.append(nums[que[0]])
        
        return result