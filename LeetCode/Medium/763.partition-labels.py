class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in last_index:
                last_index[s[i]] = i
        
        result = []
        start = 0
        end = 0
    

        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                result.append(end-start+1)
                start = i + 1
        
        return result
