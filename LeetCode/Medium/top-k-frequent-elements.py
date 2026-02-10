class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums)
        freq = defaultdict(list)
        Result = []

        for num in nums_freq:
            freq[nums_freq[num]].append(num)
        
        sorted_freq = dict(sorted(freq.items(),reverse = True))

        no_max = k
        for frq in sorted_freq:
            if no_max > 0:
                no_max -= len(sorted_freq[frq])
                Result.extend(sorted_freq[frq])
            else:
                break
                
        return Result


            

            
