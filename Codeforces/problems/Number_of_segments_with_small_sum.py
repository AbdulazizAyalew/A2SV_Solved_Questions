n, s = map(int, input().split())
a = list(map(int, input().split()))

count = 0
n = len(a)
ans = 0
window = 0
left = 0
for right in range(n):
    window += a[right]
    while window > s:
        window -= a[left]
        left += 1
    ans += right - left + 1

print(ans)
