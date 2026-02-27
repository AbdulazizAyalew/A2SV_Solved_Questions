n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
current_sum = 0
answer = 0

for r in range(n):
    current_sum += a[r]
    
    while current_sum >= s:
        answer += (n - r)
        current_sum -= a[l]
        l += 1

print(answer)
