n = int(input())
p = [int(input()) for _ in range(n-1)]

children = [[] for _ in range(n+1)]
for i in range(2, n+1):
    parent = p[i-2]
    children[parent].append(i)

for node in range(1, n+1):
    if len(children[node]) > 0: 
        leaf_count = 0
        
        for child in children[node]:
            if len(children[child]) == 0:
                leaf_count += 1
        
        if leaf_count < 3:
            print("No")
            exit()

print("Yes")