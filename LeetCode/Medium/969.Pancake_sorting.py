class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = arr[:]
        sorted_arr.sort()
        n = len(arr)
        Result = []
        # print(arr)
        while sorted_arr != arr and n != 1:
            sliced = arr[:n]
            print(sliced)
            maxx = max(sliced)
            print(maxx)
            n -= 1
            ind = 0
            for i in range(n):
                if arr[i] == maxx:
                    ind = i
                    break
            else:
                continue
            print(ind)
            left = 0
            right = ind

            while left < right:
                arr[left] , arr[right] = arr[right] , arr[left]
                left += 1
                right -= 1
            if ind == n:
                Result.append(ind + 1)
                continue
            left = 0
            right = n
            while left < right:
                arr[left] , arr[right] = arr[right] , arr[left]
                left += 1
                right -= 1
            
            
            Result.extend([ind + 1, n+1])
            
        
        return Result
            
