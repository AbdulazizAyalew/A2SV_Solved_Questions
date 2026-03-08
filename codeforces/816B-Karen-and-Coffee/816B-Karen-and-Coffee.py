# print(prefix_sum)

for _ in range(q):
    questions = list(map(int,input().split()))
    if questions[1] < minn or questions[0] > maxx:
        print(0)
    else:
        if questions[0] <= minn:
            if questions[1] <= maxx:
                print(prefix_sum[questions[1]-minn])
            else:
                print(prefix_sum[maxx-minn])
        else:
            if questions[1] <= maxx:
                print(prefix_sum[questions[1]-minn] - prefix_sum[questions[0]-minn-1])
            else:
                print(prefix_sum[maxx-minn] - prefix_sum[questions[0]-minn-1])