class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_rabs = Counter(answers)
        ans = 0
        
        for rabs in count_rabs:
            if rabs == 0:
                ans += count_rabs[rabs]
            else:
                if rabs + 1 == count_rabs[rabs]:
                    ans += rabs+ 1
                else:
                    temp = count_rabs[rabs]
                
                    while temp > rabs+1  :
                        temp -= (rabs+1)
                        ans += rabs+1
                    ans += rabs + 1
        
        return ans
