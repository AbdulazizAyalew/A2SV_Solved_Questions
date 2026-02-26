n = int(input())
points = list(map(int,input().split()))

points.sort()

if n % 2 != 0:
    print(points[n//2])
else:
    print(points[n//2 - 1])
