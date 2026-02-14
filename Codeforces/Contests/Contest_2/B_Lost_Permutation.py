for i in range(int(input())):
    m , s = map(int,input().split())
    b = list(map(int,input().split()))
    
    max_b = max(b)
    check = set(b)
    checkk = False
    for i in range(1,max_b):
        if i not in check:
            if s - i == 0:
                b.append(i)
                if len(b) == max_b:
                    print("YES")
                else:
                    print("NO")
                checkk = True
                break
            elif s - i < 0:
                print("NO")
                checkk = True
                break
            else:
                s -= i
                b.append(i)
    if checkk == True:
        continue

    j = max_b + 1
    while True:
        if s - j == 0:
            print("YES")
            break
        elif s - j < 0:
            print("NO")
            break
        else:
            s -= j
            j += 1
    
    
        