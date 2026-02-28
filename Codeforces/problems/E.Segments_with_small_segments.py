n,k = map(int,input().split())

a = list(map(int,input().split()))

count = 0
l = 0
distnicts = {}

for i in range(len(a)):
    if a[i] not in distnicts:
        distnicts[a[i]] = 1
    else:
        distnicts[a[i]] += 1
    
    while len(distnicts) > k:
        distnicts[a[l]] -= 1
        if distnicts[a[l]] == 0:
            del distnicts[a[l]]
        l += 1

    if len(distnicts) <= k:
        count += (i-l+1)


print(count) 

