t = int(input())
from collections import Counter

for i in range(t):
    n = int(input())
    s = input()
    word1 = set(s[0])
    max_unique = 0
    word_2 = Counter(s[1:])
    
    for k in range(1,len(s)):
        if s[k] == " ":
            continue
        summ = len(word1) + len(word_2)
        if summ > max_unique:
            max_unique = summ
        
        word_2[s[k]] -= 1
        if word_2[s[k]] == 0:
            del word_2[s[k]]
        word1.add(s[k])
  
    
    print(max_unique)
        