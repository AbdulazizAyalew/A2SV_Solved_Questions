for _ in range(int(input())):
    s = input()
    charr = ""
    count = 0
    sett = set()
    # if len(s) == 1:
    #     print(s[0])
    #     continue
    for i in range(len(s)):
        if i == 0:
            charr = s[i]
            count += 1
        else:
            if s[i] == charr:
                count += 1
            else:
                if count % 2 != 0:
                    sett.add(charr)
                count = 1
                charr = s[i]
    else:
        if count % 2 != 0:
            sett.add(charr)
    
    res = []
    for c in sett:
        res.append(c)
    
    res.sort()
    print("".join(res))


