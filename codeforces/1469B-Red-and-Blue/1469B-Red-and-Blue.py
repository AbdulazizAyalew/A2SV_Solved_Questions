t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    cur = 0
    max_r = 0
    for x in r:
        cur += x
        max_r = max(max_r, cur)

    cur = 0
    max_b = 0
    for x in b:
        cur += x
        max_b = max(max_b, cur)

    print(max_r + max_b)