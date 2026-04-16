class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        bucket = [[] for i in range(len(nums))]
        for n in count_nums:
            bucket[count_nums[n]-1].append(n)
        
        ans = []
        j = len(bucket) - 1
        while len(ans) < k:
            ans.extend(bucket[j])
            j -= 1

        return ans
