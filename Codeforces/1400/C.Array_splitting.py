n, k = map(int,input().split())

a = list(map(int,input().split()))

ranges = []
for i in range(n-1):
    ranges.append(a[i+1]-a[i])

ranges.sort()
# min_cost = 0
for j in range(k-1):
    ranges.pop()

print(sum(ranges))
