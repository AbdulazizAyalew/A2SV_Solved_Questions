class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count_s1 = Counter(s1)
        count_s2 = Counter(s2)
        for w in count_s1:
            if w in count_s2:
                check = abs(count_s1[w] - count_s2[w])
                if check % 2 != 0:
                    return -1
            else:
                if count_s1[w] % 2 != 0:
                    return -1        

        xy_pairs = 0
        xx_pairs = 0
        i = 0
        j = 1
        while j < len(s1):
            if s1[i] == s2[i]:
                i += 1
                if i == j:
                    j += 1
            else:
                if s1[j] == s2[j]:
                    j += 1
                else:
                    if ( s1[i] + s1[j] == "xy" and s2[i] + s2[j] == "yx" ) or ( s1[i] + s1[j] == "yx" and s2[i] + s2[j] == "xy"):
                        xy_pairs += 1
                    elif (s1[i] + s1[j] == "xx" and s2[i] + s2[j] == "yy") or (s1[i] + s1[j] == "yy" and s2[i] + s2[j] == "xx"):
                        xx_pairs += 1
                    i = j + 1
                    j = i + 1
        
        if xy_pairs % 2 != 0:
            return xy_pairs + 1 + xx_pairs
        else:
            return xy_pairs + xx_pairs
