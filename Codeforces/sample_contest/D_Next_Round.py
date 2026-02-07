n,k = map(int,(input().split()))
no_partc = 0
contestants = list(map(int,input().split()))
score_lim = contestants[k-1]

for contestant in contestants:
    if contestant > 0 and contestant >= score_lim:
        no_partc += 1

print(no_partc)
