class Solution:
    def customSortString(self, order: str, s: str) -> str:
        new_s = []
        s_char = Counter(s)
        ord_c = set(order)

        for ch in order:
            if ch in s_char:
                new_s.extend([ch]* s_char[ch])
                
        
        for c in s_char:
            if c not in ord_c:
                new_s.extend([c]*s_char[c])
        
        return "".join(new_s)