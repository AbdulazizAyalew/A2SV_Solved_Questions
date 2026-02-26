for _ in range(int(input())):
    n , k = map(int,input().split())
    casinos = []
    for i in range(n):
        casino = list(map(int,input().split()))
        casinos.append(casino)
 
    # print(casinos)
    first_sort = []
    for i in range(len(casinos)):
        first_sort.append([casinos[i][2],casinos[i][0],casinos[i][1]])
    
    first_sort.sort(reverse=True)
    second_sort = []
    for j in range(n):
        second_sort.append([first_sort[j][1],first_sort[j][2],first_sort[j][0]])
    
    second_sort.sort()
    # print(second_sort)
 
    for i in range(n):
        if second_sort[i][0] <= k and second_sort[i][1] >= k:
            if second_sort[i][2] > k:
                k = second_sort[i][2]
    
    print(k)
