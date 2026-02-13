for _ in range(int(input())):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    prefix = 0
    first_hit = -1
    cycle_len = -1
    
    
    for i in range(n):
        if s[i] == 'L':
            prefix -= 1
        else:
            prefix += 1
        
        if prefix == -x and first_hit == -1:
            first_hit = i + 1
        
        if prefix == 0 and cycle_len == -1:
            cycle_len = i + 1
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    answer = 1
    remaining = k - first_hit
    
    if cycle_len == -1:
        print(answer)
        continue
    
    answer += remaining // cycle_len
    
    print(answer)
