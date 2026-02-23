from collections import Counter
t = int(input())


for i in range(t):
    s = input()
    t = input()
    
    answer = []
    s_chars = Counter(s)
    t_chars = Counter(t)
    Impossible = False

    for ch in s_chars:
        if ch not in t_chars or s_chars[ch] > t_chars[ch]:
            Impossible = True
            
        t_chars[ch] -= s_chars[ch]
    
    if Impossible != True:
        for c in t_chars:
            answer.extend([c]*t_chars[c])
        answer.sort()

        s_po = 0
        t_po = 0
        
        while s_po < len(s):
            if t_po < len(answer):
                if s[s_po] <= answer[t_po]:
                    
                    answer.insert(t_po,s[s_po])
                    s_po += 1
                t_po += 1
            else:
                answer.append(s[s_po])
                s_po += 1
                t_po += 1
        print("".join(answer))
    else:
        print("Impossible")
 
