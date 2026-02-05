class Solution(object):
    def removeComments(self, source):
        Block_comment = False
        Result = []
        code = ""

        for line in source:
            i = 0
            if not Block_comment:
                code = ""

            while i < len(line):
                if Block_comment:
                    if i + 1 < len(line) and line[i] == "*" and line[i + 1] == "/":
                        Block_comment = False
                        i += 2
                    else:
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == "/" and line[i + 1] == "/":
                        break

                    elif i + 1 < len(line) and line[i] == "/" and line[i + 1] == "*":
                        Block_comment = True
                        i += 2

                    else:
                        code += line[i]
                        i += 1

            if not Block_comment and code:
                Result.append(code)

        return Result
