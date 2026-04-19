
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(arr1,arr2):
            l = 0
            r = 0
            new_arr = []
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

        def merge(arr):
            if len(arr) <= 1:
                  return arr
            
            n = len(arr) // 2
            left = merge(arr[:n])
            right = merge(arr[n:])

            return mergeSort(left,right)
        
        nums = []
        ptr = head
        while ptr:
            nums.append(ptr.val)
            ptr = ptr.next


        arr = merge(nums)

        result = []
        First = ListNode()
        for i in range(len(arr)):
            curr = ListNode(arr[i])
            if i == 0:
                First = curr
            else:
                prev.next = curr
            
            prev = curr

        return First if head else head
