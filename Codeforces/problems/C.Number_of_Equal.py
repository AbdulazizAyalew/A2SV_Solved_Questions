from collections import Counter
n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

pairs = {}

for i in range(len(a)):
    if a[i] not in pairs:
        pairs[a[i]] = [1,0]
    else:
        pairs[a[i]][0] += 1

for j in range(len(b)):
    if b[j] in pairs:
        pairs[b[j]][1] += 1

count = 0

for p in pairs:
    count += (pairs[p][0] * pairs[p][1])

print(count)
