class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        Result = {}
        info_holder = {}

        for path in paths:
            splitted_path_info = path.split()
            info_holder[splitted_path_info[0]] = []
            for i in range(1,len(splitted_path_info)):
                content_info = splitted_path_info[i].split(".")
                number = content_info[0]
                content = ""
                for k in range(4,len(content_info[1])):
                    if content_info[1][k] != ")":
                        content += content_info[1][k]
                    else:
                        break
                if splitted_path_info[0] in info_holder:
                    info_holder[splitted_path_info[0]].append({"c":content,"n":number})
                else:
                    info_holder[splitted_path_info[0]] = [{"c":content,"n":number}]
        
        
        for path_inf in info_holder:
            for content in info_holder[path_inf]:
                cont_2_find = content["c"]
                num = content["n"]
                s = path_inf + "/" + str(num) + ".txt"

                if cont_2_find not in Result:
                    Result[cont_2_find] = [s]
                else:
                    Result[cont_2_find].append(s)
        Answer = []
        for res in Result:
            if len(Result[res]) > 1:
                Answer.append(Result[res])
        
        return Answer

                



             
