class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            diff.append([costs[i][0]-costs[i][1],i])
        ans = 0

        diff.sort()
        print(diff)
        for i in range(len(diff)//2):
            ans += (costs[diff[i][1]][0])
        
        for j in range(len(diff)//2,len(diff)):
            ans += (costs[diff[j][1]][1])
        
        return ans



