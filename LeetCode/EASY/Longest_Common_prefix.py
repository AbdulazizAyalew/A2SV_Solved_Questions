class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = len(strs[0])
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        result = ""
        for j in range(min_len):
            check_char = strs[0][j]
            for i in range(len(strs)):
                if strs[i][j] != check_char:
                    return result
            else:
                result += check_char

        return result
        