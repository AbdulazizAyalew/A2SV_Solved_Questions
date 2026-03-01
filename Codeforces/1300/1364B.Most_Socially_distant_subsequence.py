t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    subseq = [p[0]] 
    
    for i in range(1, n-1):
        if (p[i-1] < p[i] > p[i+1]) or (p[i-1] > p[i] < p[i+1]):
            subseq.append(p[i])
    
    subseq.append(p[-1]) 
    
    print(len(subseq))
    print(*subseq)
