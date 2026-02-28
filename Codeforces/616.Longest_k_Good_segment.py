n,k = map(int,input().split())

a = list(map(int,input().split()))


unique_num = {}
l = 0
max_count = 0
ans = [1,1]

for i in range(len(a)):
    if a[i] not in unique_num:
        unique_num[a[i]] = 1
    else:
        unique_num[a[i]] += 1
    
    while len(unique_num) > k:
        unique_num[a[l]] -= 1
        if unique_num[a[l]] == 0:
            del unique_num[a[l]]
        l += 1
    
    if max_count < i - l + 1:
        max_count = i - l + 1
        ans[0] = l + 1
        ans[1] = i + 1

print(f"{ans[0]} {ans[1]}")
