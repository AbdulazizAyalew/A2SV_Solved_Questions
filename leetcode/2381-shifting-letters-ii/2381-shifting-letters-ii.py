from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for l, r, d in shifts:
            if d == 1:
                diff[l] += 1
                diff[r + 1] -= 1
            else:
                diff[l] -= 1
                diff[r + 1] += 1

        for i in range(1, n):
            diff[i] += diff[i - 1]

        res = []

        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + diff[i]) % 26 + ord('a'))
            res.append(new_char)

        return "".join(res)