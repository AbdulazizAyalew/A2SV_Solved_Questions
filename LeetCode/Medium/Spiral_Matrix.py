class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        To_Left = False
        To_Right = True
        To_Up = False
        To_Down = False
        m = len(matrix[0]) #number of columns
        n = len(matrix) #number of Rows
        curr_indx = 0
        k = m - 1
        j = 0
        Result = []

        if m == 1:
            for num in matrix:
                Result.extend(num)
            return Result
            

        level_status = defaultdict(lambda: [0, k+1])
        
        while To_Left or To_Right or To_Up or To_Down:
            if To_Right:
                for i in range(j,k+1):
                    Result.append(matrix[curr_indx][i])
                level_status[curr_indx] = [0,0]
                To_Right = False
                if curr_indx + 1 < n and level_status[curr_indx + 1] != [0,0]:
                    print("l")
                    To_Down = True
                    curr_indx += 1
                
            elif To_Down:
                Result.append(matrix[curr_indx][k])
                level_status[curr_indx][1] -= 1
                if curr_indx + 1 < n and level_status[curr_indx + 1] != [0,0]:
                    curr_indx += 1
                else:
                    To_Down = False                
                    if k != j:
                        k -= 1
                        To_Left = True
                
            
            elif To_Left:
                for s in range(k,j-1,-1):
                    Result.append(matrix[curr_indx][s])

                level_status[curr_indx] = [0,0]
                To_Left = False
                if level_status[curr_indx - 1] != [0,0]:
                    curr_indx -= 1
                    To_Up = True
            elif To_Up:
                Result.append(matrix[curr_indx][j])
                level_status[curr_indx][0] += 1
                if level_status[curr_indx - 1] != [0,0]:
                    curr_indx -= 1
                else:
                    To_Up = False
                    if k != j:
                        To_Right = True
                        j += 1

        return Result

                


        
