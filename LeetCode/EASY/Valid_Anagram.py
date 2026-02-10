class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)

        # Compare similarities of each key - value pair on both Dictionaries
        if count_t != count_s:
            return False
        return True
        
