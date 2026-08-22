class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
           return s
        output = [[] for _ in range(numRows)]
        j = 0
        for i in range(numRows):
            output[i].append(s[i])
        j = numRows
        flag = True
        while j < len(s):
            if flag:
                for i in range(len(output)-2, -1, -1):
                    if j < len(s):
                        output[i].append(s[j])
                        j+= 1
                    else:
                        break
                flag = not flag
            if not flag:
                for i in range(1, len(output)):
                    if j < len(s):
                        output[i].append(s[j])
                        j+= 1
                    else:
                        break
                flag = not flag
        return "".join("".join(rows) for rows in output)