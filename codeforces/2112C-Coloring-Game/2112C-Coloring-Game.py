for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()
    ans = 0
    max_val = a[-1]
        
    for k in range(2, n):
        need = max(a[k], max_val - a[k])
        
        l, r = 0, k - 1
            
        while l < r:
            if a[l] + a[r] > need:
                ans += (r - l)
                r -= 1
            else:
                l += 1
    
    print(ans)