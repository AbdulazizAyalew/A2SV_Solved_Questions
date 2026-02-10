class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Result = []
        anagrams_pair = {}

        for s in strs:
            srt_s = "".join(sorted(s))
            if srt_s in anagrams_pair:
                anagrams_pair[srt_s].append(s)
            else:
                anagrams_pair[srt_s] = [s]

        for anagram in anagrams_pair:
            Result.append(anagrams_pair[anagram])

        return Result
