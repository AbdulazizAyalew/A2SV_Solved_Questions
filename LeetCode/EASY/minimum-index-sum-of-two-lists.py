class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set_list2 = {}
        result = []
        min_sum_index = len(list1) + len(list2)
        for j in range(len(list2)):
            set_list2[list2[j]] = j

        for i in range(len(list1)):
            if list1[i] in set_list2:
                sum_index = i + set_list2[list1[i]]
                if sum_index < min_sum_index:
                    result = []
                    result.append(list1[i])
                    min_sum_index = sum_index
                elif sum_index == min_sum_index:
                    result.append(list1[i])
        return result
    
