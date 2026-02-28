from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    if a == b:
        print("YES")
        continue
    change = 0
    count_a = Counter(a)
    if len(count_a) == 1:
        print("NO")
        continue

    for j in range(n-1,-1,-1):
        if count_a["0"] == count_a["1"]:
            if change == 0:
                if a[j] != b[j]:
                    change = 1
            else:
                if a[j] == "0":
                    if "1" != b[j]:
                        change = 0
                else:
                    if "0" != b[j]:
                        change = 0
            
        else:
            if change == 0:
                if a[j] != b[j]:
                    print("NO")
                    break
            else:
                if a[j] == "0":
                    if "1" != b[j]:
                        print("NO")
                        break
                else:
                    if "0" != b[j]:
                        print("NO")
                        break
        count_a[a[j]] -= 1
        
    else:
        print("YES")
