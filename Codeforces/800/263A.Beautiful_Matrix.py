
matrix = []
for i in range(5):
    row = list(map(int,input().split()))
    matrix.append(row)

indx = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            indx = [i+1,j+1]
            break
    else:
        continue
    break
move = (abs(3-indx[0]) + abs(3-indx[1]))
print(move)

