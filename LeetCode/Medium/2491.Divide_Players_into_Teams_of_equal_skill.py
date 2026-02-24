class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        R = len(skill) - 1
        summ = 0
        Chem = 0
        while l < R:
            if l == 0:
                summ = skill[l] + skill[R]
            else:
                if skill[l] + skill[R] != summ:
                    Chem = -1
                    break
            Chem += (skill[l] * skill[R])
            l += 1
            R -= 1
        return Chem 