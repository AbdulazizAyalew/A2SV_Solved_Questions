for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()

    count_c = {}
    min_ans = 9999999999999999
    l = 0
    for i in range(len(s)):
        if s[i] not in count_c:
            count_c[s[i]] = 1
        else:
            count_c[s[i]] += 1
        
        while i - l + 1 > k:
            count_c[s[l]] -= 1
            if count_c[s[l]] == 0:
                del count_c[s[l]]
            l += 1
        
        if i - l + 1 == k:
            if "W" in count_c:
                min_ans = min(count_c["W"],min_ans)
            else:
                min_ans = 0
        
    
    print(min_ans)


