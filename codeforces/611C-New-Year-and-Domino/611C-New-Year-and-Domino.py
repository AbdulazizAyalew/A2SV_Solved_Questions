h,w = map(int,input().split())
grid = []

for _ in range(h):
    row = input()
    grid.append(row)

row_prefix = []
summ = 0

for i in range(h):
    row = []
    Total_row = 0
    for j in range(w):
        if grid[i][j] == ".":
            if summ > 0:
                Total_row += 1
            summ += 1
        else:
            summ = 0
        row.append(Total_row)
    row_prefix.append(row)

col_prefix = []
summ = 0

for i in range(w):
    col = []
    Total_col = 0
    for j in range(h):
        if grid[j][i] == ".":
            if summ > 0:
                Total_col += 1
            summ += 1
        else:
            summ = 0
        col.append(Total_col)
    col_prefix.append(col)


q = int(input())
for _ in range(q):
    query = list(map(int,input().split()))
    Tot_rows = 0
    for i in range(query[0]-1,query[2]):
        Tot_rows += row_prefix[i][query[3]-1]
        if row_prefix[i][query[1]-1] != 0:
            Tot_rows -= row_prefix[i][query[1]-1]
    
    Tot_cols = 0
    for j in range(query[1]-1,query[3]):
        Tot_cols += col_prefix[j][query[2]-1]
        if col_prefix[j][query[0]-1] != 0:
            Tot_cols -= col_prefix[j][query[0]-1]
    
    print(Tot_rows + Tot_cols)