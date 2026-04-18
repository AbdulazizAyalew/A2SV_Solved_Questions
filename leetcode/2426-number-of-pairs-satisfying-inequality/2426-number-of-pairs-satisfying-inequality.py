class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])
        inversion = 0
        
        def merge(arr1,arr2):
            nonlocal inversion
            l = 0
            r = 0
            new_arr = []
            j = 0
            for i in range(len(arr1)):
                while j < len(arr2) and arr1[i] > arr2[j] + diff:
                    j += 1
                inversion += (len(arr2) - j)

            while l < len(arr1) and r < len(arr2):
                if arr1[l] <= arr2[r]:
                    new_arr.append(arr1[l])
                    l += 1
                else:
                    new_arr.append(arr2[r])
                    r += 1
            new_arr.extend(arr1[l:])
            new_arr.extend(arr2[r:])
            return new_arr
        
        def mergeSort(Arr):
            if len(Arr) == 1:
                return Arr
            
            n = len(Arr) // 2
            left = mergeSort(Arr[:n])
            right = mergeSort(Arr[n:])

            return merge(left,right)
        
        mergeSort(arr)
        return inversion