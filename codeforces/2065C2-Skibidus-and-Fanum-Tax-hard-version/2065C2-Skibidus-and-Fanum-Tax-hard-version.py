def lower_bound(arr, target):
        low, high = 0, len(arr) - 1
        ans = len(arr)
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
    
    prev = -10**18
    possible = True
    
    for x in a:
        best = float('inf')
        
        if x >= prev:
            best = x
        
        target = prev + x
        idx = lower_bound(b, target)
        
        if idx < m:
            best = min(best, b[idx] - x)
        
        if best == float('inf'):
            possible = False
            break
        
        prev = best

    print("YES" if possible else "NO")