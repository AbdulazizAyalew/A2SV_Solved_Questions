class Solution(object):
    def removeComments(self, source):
        Block_comment = False
        Result = []
        line_code = []
        code = ""

        for i in range(len(source)):

            j = 0
            if not Block_comment:
                line_code = []

            while j < len(source[i]):
                if not Block_comment:
                    if j + 1 < len(source[i]) and source[i][j] == "/" and source[i][j + 1] == "/":
                        break

                    elif j + 1 < len(source[i]) and source[i][j] == "/" and source[i][j + 1] == "*":
                        Block_comment = True
                        j += 2
                    else:
                        line_code.append(source[i][j])
                        j += 1
                else:
                    if j + 1 < len(source[i]) and source[i][j] == "*" and source[i][j + 1] == "/":
                        Block_comment = False
                        j += 2
                    else:
                        j += 1

            if not Block_comment:
                code = "".join(line_code)
                if code != "":
                    Result.append(code)
                elif code == "" and any(c == " " for c in line_code):
                    Result.append(code)

        return Result
